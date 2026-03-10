# def is_even_or_odd(n):
#     if n%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# def add_num(a,b):
#     return a+b
#
# def div(a,b):
#     return a/b

from fpdf import FPDF

# Data for the 10 Practice Papers
papers = [
    {
        "title": "Practice Paper 1",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. Name two examples each of Kharif crops and Rabi crops.
2. What are the advantages of using CNG and LPG as fuels?
3. Define ignition temperature.
4. What is the audible range of frequencies for a normal human ear?

Section B (4 Marks each)
5. Explain how fertilizers are different from manure.
6. Describe the process of formation of petroleum.
7. Differentiate between internal fertilization and external fertilization.

Section C (5 Marks each)
8. Explain why sliding friction is less than static friction.
9. Make a labelled diagram of a candle flame and explain its three zones."""
    },
    {
        "title": "Practice Paper 2",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What are antibiotics? Name the first antibiotic discovered.
2. Define atmospheric pressure.
3. Why are the handles of cricket bats and tennis racquets covered with rough tape?
4. What is the 'Adam's apple'?

Section B (4 Marks each)
5. Explain why fossil fuels are exhaustible natural resources.
6. List changes in the body that take place at puberty.
7. Explain why objects moving in fluids must have special shapes.

Section C (5 Marks each)
8. Describe the construction and working of a human eye with a labelled sketch.
9. What is irrigation? Describe two methods of irrigation which conserve water."""
    },
    {
        "title": "Practice Paper 3",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. State the laws of reflection.
2. What is the difference between a Zygote and a Foetus?
3. Name the unit in which the calorific value of a fuel is expressed.
4. What is the Red Data Book?

Section B (4 Marks each)
5. Explain the process of electroplating. Give two real-life examples.
6. Differentiate between a wildlife sanctuary and a biosphere reserve.
7. Explain in what way noise pollution is harmful to humans.

Section C (5 Marks each)
8. Describe an experiment to show that air (oxygen) is essential for burning.
9. Write a short paragraph on the following agricultural practices:
   (a) Preparation of soil
   (b) Weeding"""
    },
    {
        "title": "Practice Paper 4",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What is meant by the 'time period' of a pendulum?
2. Why is it difficult to burn a heap of green leaves but dry leaves catch fire easily?
3. Define metamorphosis.
4. Give two examples of situations in which applied force causes a change in the shape of an object.

Section B (4 Marks each)
5. Suggest three measures to protect ourselves from lightning.
6. Explain how CO2 is able to control fires.
7. Define asexual reproduction. Describe two methods of asexual reproduction in animals.

Section C (5 Marks each)
8. Explain the nitrogen cycle with the help of a schematic diagram.
9. Draw a diagram to show the position of the image formed by a plane mirror. List the characteristics of the image formed."""
    },
    {
        "title": "Practice Paper 5",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What are weeds? How can we control them?
2. Which part of the flame does a goldsmith use for melting gold and silver and why?
3. What is lateral inversion?
4. Name the petroleum product used for surfacing roads.

Section B (4 Marks each)
5. Explain why sportsmen use shoes with spikes.
6. What are sex hormones? Why are they named so? State their function.
7. Describe how coal is formed from dead vegetation. What is this process called?

Section C (5 Marks each)
8. Describe an activity to show that liquids conduct electricity. (Include a circuit diagram).
9. Explain the consequences of deforestation on:
   (a) Wild animals
   (b) The next generation"""
    },
    {
        "title": "Practice Paper 6",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. Define fermentation.
2. Why should we conserve biodiversity?
3. Mention two methods to increase friction.
4. What is the function of the retina in the human eye?

Section B (4 Marks each)
5. Sketch the larynx and explain its function in your own words.
6. Explain the difference between contact and non-contact forces with examples.
7. What is menstruation? Explain.

Section C (5 Marks each)
8. Prepare a list of objects around you that are electroplated. Explain the method of coating silver on a spoon.
9. What are the major groups of microorganisms? Write short lines on the usefulness of microorganisms in our lives."""
    },
    {
        "title": "Practice Paper 7",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What is the Richter scale?
2. Name the male and female gametes in humans.
3. Why is water not used to control fires involving electrical equipment?
4. What is a constellation? (Or: What is the blind spot?)

Section B (4 Marks each)
5. Explain the characteristics and uses of coke.
6. How does sex determination happen in an unborn baby?
7. Differentiate between regular and diffused reflection. Does diffused reflection mean the failure of the laws of reflection?

Section C (5 Marks each)
8. Explain the factors affecting friction. How does lubrication reduce friction?
9. Describe the process of harvesting and threshing in crop production."""
    },
    {
        "title": "Practice Paper 8",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What is a vaccine? How does it work?
2. Name the forces acting on a plastic bucket containing water held above ground level in your hand.
3. What is the relation between loudness and amplitude?
4. Define the term 'Endangered Species'.

Section B (4 Marks each)
5. Explain why a charged balloon is repelled by another charged balloon whereas an uncharged balloon is attracted by another charged balloon.
6. Compare LPG and wood as fuels.
7. Explain the importance of reproduction in organisms.

Section C (5 Marks each)
8. Draw a labelled sketch of the human eye and explain the function of the iris and pupil.
9. Outline the process of refining petroleum. Name any three constituents of petroleum and their uses."""
    },
    {
        "title": "Practice Paper 9",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What is pasteurization?
2. Why do we slip when we step on a banana peel?
3. State two differences between eukaryotes and prokaryotes (or Zygote and Foetus).
4. What are the effects of force?

Section B (4 Marks each)
5. Explain the harmful effects of noise pollution.
6. Describe the construction of a kaleidoscope.
7. Why are endocrine glands called ductless glands? Name the hormone secreted by the adrenal gland.

Section C (5 Marks each)
8. What is an earthquake? List three states in India where earthquakes are more likely to strike.
9. Explain how the use of CNG in automobiles has reduced pollution in our cities. Compare it with diesel/petrol."""
    },
    {
        "title": "Practice Paper 10",
        "content": """Max Marks: 30
Instructions: All questions are compulsory.

Section A (2 Marks each)
1. What is the greenhouse effect?
2. Give two examples of communicable diseases.
3. What is meant by 1 Hz frequency?
4. Name the instrument used to detect a charged body.

Section B (4 Marks each)
5. Explain why the sliding friction is less than the static friction.
6. Describe the process of fertilization in human beings.
7. What are the causes and consequences of deforestation?

Section C (5 Marks each)
8. Explain the chemical effects of electric current. Describe an experiment to show the chemical effect using water and electrodes.
9. Write a short note on:
   (a) Sowing of seeds
   (b) Storage of produce"""
    }
]


class PDF(FPDF):
    def header(self):
        # Font for the header
        self.set_font('Arial', 'B', 14)
        # Title
        self.cell(0, 10, self.title_text, 0, 1, 'C')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)

        # FIX: Replace any remaining smart characters that might cause errors
        # Replaces smart quotes with straight quotes, and en-dashes with hyphens
        body = body.replace(u"\u2018", "'").replace(u"\u2019", "'")
        body = body.replace(u"\u201c", '"').replace(u"\u201d", '"')
        body = body.replace(u"\u2013", "-").replace(u"\u2014", "-")

        # Output justified text
        self.multi_cell(0, 8, body)
        self.ln()


# Generate the PDFs
for i, paper in enumerate(papers):
    pdf = PDF()
    pdf.title_text = paper['title']
    pdf.add_page()

    # Add content
    pdf.chapter_body(paper['content'])

    # Save the file
    filename = f"Science_Practice_Paper_{i + 1}.pdf"
    pdf.output(filename)
    print(f"Generated: {filename}")

print("\nAll 10 practice papers have been generated successfully!")