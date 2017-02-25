import requests
import bs4
from project import db


class Strain(db.Model):

	__tablename__ = "strains"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	image = db.Column(db.Text)
	strain_type = db.Column(db.Text)
	medicinal_traits = db.Column(db.Text)
	description = db.Column(db.Text)
	inflammation = db.Column(db.Boolean)
	headache = db.Column(db.Boolean)
	spasm = db.Column(db.Boolean)
	appetite = db.Column(db.Boolean)
	anxiety = db.Column(db.Boolean)
	depression = db.Column(db.Boolean)
	insomnia = db.Column(db.Boolean)
	pain = db.Column(db.Boolean)

	def __init__(self, name, image, strain_type, medicinal_traits, description, inflammation, headache, spasm, appetite, anxiety, depression, insomnia, pain):
		self.name = name
		self.image = image
		self.strain_type = strain_type
		self.medicinal_traits = medicinal_traits
		self.description = description
		self.inflammation = inflammation
		self.headache = headache
		self.spasm = spasm
		self.appetite = appetite
		self.anxiety = anxiety
		self.depression = depression
		self.insomnia = insomnia
		self.pain = pain

url = "https://marqaha.herokuapp.com/gallery/flowers/"

if __name__ == '__main__':
	

	for page in range(1, 1491):
		
		this_link = url + str(page)
		data = requests.get(this_link)
		soup = bs4.BeautifulSoup(data.text, "html.parser")

		try:
			if soup.findAll(id='details_lineage')[0].text:

				if str(soup.find('title').text) != str("The page you were looking for doesn't exist (404)"):
					image = list(soup.find(id = 'details_image'))[0].next['src']

					# Checking to see if the picture has an image
					if str(image) != str("/images/noimg.png?1435530229"):
						print(page)
						# Getting name
						raw_name = soup.find(id='details_product_name').text
						name = raw_name.strip()

						# Getting strain_type
						strain_type = soup.find(id='details_product_sativa_indica').text

						# Getting medicinal_traits_raw, medicinal_traits
						medicinal_traits_raw = soup.findAll(id='details_lineage')[0].text
						medicinal_traits = medicinal_traits_raw.replace(", ", "|")

						# Getting description
						description = list(soup.find(id='reviews_wrap'))[3].text

						# Getting trait booleans
						inflammation = False
						if "Inflammation" in medicinal_traits:
							inflammation = True
						headache = False
						if "Headaches" or "Migraines" in medicinal_traits:
							headache = True
						spasm = False
						if "Muscle Spasms" or "Seizures" in medicinal_traits:
							spasm = True
						appetite = False
						if "Appetite" in medicinal_traits:
							appetite = True
						anxiety = False
						if "Anxiety" or "Social Anxiety" in medicinal_traits:
							anxiety = True
						depression = False
						if "Depression" in medicinal_traits:
							depression = True
						insomnia = False
						if "Sleepy" or "Insomnia" in medicinal_traits:
							insomnia = True
						pain = False
						if "Severe Pain" or "Chronic Pain" or "Pain Management" in medicinal_traits:
							pain = True
					else:
						continue

				else:
					continue
		except IndexError as e:
			continue

		new_strain = Strain(name, image, strain_type, medicinal_traits_raw, description, inflammation, headache, spasm, appetite, anxiety, depression, insomnia, pain)
		db.session.add(new_strain)
		db.session.commit()





