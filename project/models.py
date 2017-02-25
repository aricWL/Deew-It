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