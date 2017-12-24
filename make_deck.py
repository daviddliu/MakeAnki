import genanki
import pdf2image
import ipdb

# Import pdf
images = pdf2image.convert_from_path('histology_flash_cards.pdf')[11:]
# images = pdf2image.convert_from_path('Inflammation CCs.pdf')

# Make deck
my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_deck = genanki.Deck(
  2059400110,
  'Histology flash cards')

# Add cards
file_names = ["{}.jpg".format(i) for i in range(1, len(images))]
i = 1
while i < len(file_names):
    images[i-1].save(file_names[i-1], "JPEG", quality=80, optimize=True, progressive=True)
    images[i].save(file_names[i], "JPEG", quality=80, optimize=True, progressive=True)

    my_note = genanki.Note(
      model=my_model,
      fields=['<img src="{}">'.format(file_names[i-1]), '<img src="{}">'.format(file_names[i])])

    my_deck.add_note(my_note)
    i += 2

my_package = genanki.Package(my_deck)
my_package.media_files = file_names

my_package.write_to_file('histology_flash_cards.apkg')
