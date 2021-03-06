import requests
import bs4
from project import db
from project.models import Strain

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





