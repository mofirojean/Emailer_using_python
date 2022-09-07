"""
 ***********************************************
 Generates a word document from the template file
 ***********************************************
"""
from msoffice2pdf import convert
from docxtpl import DocxTemplate


class GenerateTemplate:
    """Initialize parameters"""
    def __init__(self, userName, companyName):
        self.name = userName
        self.companyName = companyName

    # Generates the document and saves it in the Docs folder
    def generateTemplate(self):
        doc = DocxTemplate("./Template/Template.docx")
        context = {'company': self.companyName, 'name': self.name}
        doc.render(context)
        doc.save(f"./Docs/{self.name}.docx")
        output = convert(source=f"./Docs/{self.name}.docx", output_dir="./Docs_Pdf/", soft=1)
        print(output)

        return output


# Driver Method
generate = GenerateTemplate("mofiro", "NerdTech")
generate.generateTemplate()
