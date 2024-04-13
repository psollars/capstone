from langchain_core.documents.base import Document


responses = [
    {
        "query": "Who is the instructor for the SQL and Databases class?",
        "result": "Graham Hukill (gshukill@umich.edu)",
        "source_documents": [
            Document(
                page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
                metadata={
                    "source": "511_2023-10.md",
                    "heading": "Student Services",
                    "section": "17",
                    "course_number": "SIADS 511",
                    "course_title": "SQL and Databases",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
                },
            ),
            Document(
                page_content="SQL and Databases (SIADS 511), Student Mental Health: Refer to the University's Resources for Stress and Mental Health website for a listing of resources for students.",
                metadata={
                    "source": "511_2023-10.md",
                    "heading": "Student Mental Health",
                    "section": "16",
                    "course_number": "SIADS 511",
                    "course_title": "SQL and Databases",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
                },
            ),
        ],
    },
    {
        "query": "What classes does Graham Hukill teach?",
        "result": "Graham Hukill teaches Database Architecture & Technology (SIADS 611) and SQL and Databases (SIADS 511).",
        "source_documents": [
            Document(
                page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
                metadata={
                    "source": "511_2023-10.md",
                    "heading": "Student Services",
                    "section": "17",
                    "course_number": "SIADS 511",
                    "course_title": "SQL and Databases",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
                },
            ),
            Document(
                page_content="SQL and Databases (SIADS 511), Student Mental Health: Refer to the University's Resources for Stress and Mental Health website for a listing of resources for students.",
                metadata={
                    "source": "511_2023-10.md",
                    "heading": "Student Mental Health",
                    "section": "16",
                    "course_number": "SIADS 511",
                    "course_title": "SQL and Databases",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
                },
            ),
            Document(
                page_content="SQL and Databases (SIADS 511), Course Outcomes: 1. Learn the SQL Language\n2. Learn relational database design\n3. Learn how to load and normalize data in databases\n4. Learn how to add indexes for performance\n5. Learn about stored procedures\n6. Learn Regular Expressions for scanning, parsing, and extracting data",
                metadata={
                    "source": "511_2023-10.md",
                    "heading": "Course Outcomes",
                    "section": "7",
                    "course_number": "SIADS 511",
                    "course_title": "SQL and Databases",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
                },
            ),
        ],
    },
    {
        "query": "How many credits do I need to complete the MADS program?",
        "result": "You need to complete a minimum of 34 credit hours of SIADS coursework to earn a Master of Applied Data Science degree at the University of Michigan School of Information.",
        "source_documents": [
            Document(
                page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
                metadata={
                    "source": "advising_guide.md",
                    "heading": "Graduation > Q: When should I apply for graduation?",
                    "section": "48",
                    "course_number": "n/a",
                    "course_title": "n/a",
                    "course_date": "n/a",
                    "document": "https://docs.google.com/document/d/1A3zdTF0AYQY_zzD2-OlpSHeDxnWqFVEhXl446SyT_pA/edit",
                },
            ),
            Document(
                page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
                metadata={
                    "source": "handbook.md",
                    "heading": "MADS Slack Policy, Standards, and Practices > MADS Slack Standards and Processes > Use of Slack",
                    "section": "55",
                    "course_number": "n/a",
                    "course_title": "n/a",
                    "course_date": "n/a",
                    "document": "https://docs.google.com/document/d/1YEOcpdONdme5kmpNEnZpdbJeVFhEIw1pS0wq16QdH1I/edit",
                },
            ),
        ],
    },
    {
        "query": "How does PCA work?",
        "result": "PCA (Principal Component Analysis) is a statistical procedure...",
        "source_documents": [
            Document(
                page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
                metadata={
                    "source": "06_machine-learning-in-the-cloud.en.txt",
                    "course_number": "SIADS 673",
                    "course_title": "Cloud Computing",
                    "start_index": 942,
                },
            ),
        ],
    },
]
