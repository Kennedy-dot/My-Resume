from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resume', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()

pdf.add_page()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

# Your contact information
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Kennedy Musyoka', 0, 1, 'L')
pdf.cell(0, 10, 'Kennedymusyoka2002@gmail.com', 0, 1, 'L') 
pdf.cell(0, 10, '0111602678', 0, 1, 'L')
pdf.ln(10)

# Professional Summary
pdf.chapter_title('Professional Summary')
summary = "Experienced professional with a proven track record in software development..."
pdf.chapter_body(summary)

# Work Experience
pdf.chapter_title('Work Experience')
work_experience = """Software Engineer at KenTech Company
- Developed web applications using Python and JavaScript.
- Led a team of 5 developers to complete project library system on time.

Junior Developer at KenTech coding Company
- Assisted in developing mobile applications using Java.
- Participated in code reviews and debugging sessions.
"""
pdf.chapter_body(work_experience)

# Education
pdf.chapter_title('Education')
education = """Bachelor of Science in Computer Science
University of Pwani, 2022-2026
"""
pdf.chapter_body(education)

# Skills
pdf.chapter_title('Skills')
skills = "Python, JavaScript, Java, SQL, Team Leadership, Communication"
pdf.chapter_body(skills)

# Output PDF
pdf.output('resume.pdf')

