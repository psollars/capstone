from langchain_core.documents.base import Document


responses = [
    # What is a backpack?
    {
        "query": "What is a backpack?",
        "result": "\n    In the context of Wolverine Access, a backpack is a feature that allows students to prepare for their upcoming registration appointment by filling it with classes they want to take. When it is time to register, students will select one or more classes from their Backpack to register for it. Note that placing a class in your Backpack does not enroll you in that class. You must register for a class to become enrolled in it. It's important to note that receiving an override does not enroll you in the course, you still must register through Wolverine Access to claim the seat that has been opened for you.",
        "source_documents": [
            Document(
                page_content='Class Registration > Q: What is a Backpack?: A: The Backpack is a feature available on [Wolverine Access](https://wolverineaccess.umich.edu/) that works much like the "shopping carts" you have seen on many retail websites. With the Backpack you can prepare for your upcoming registration appointment by filling it with classes you want to take. When it is time to register, you will select one or more classes from your Backpack to register for it. NOTE: Placing a class in your Backpack does not enroll you in that class. You must register for a class to become enrolled in it. It is important to note that receiving an override does not enroll you in the course, you still must register through [Wolverine Access](https://wolverineaccess.umich.edu/) to claim the seat that has been opened for you.',
                metadata={
                    "source": "advising_guide.md",
                    "heading": "Class Registration > Q: What is a Backpack?",
                    "section": "21",
                    "course_number": "n/a",
                    "course_title": "n/a",
                    "course_date": "n/a",
                    "document": "https://docs.google.com/document/d/1A3zdTF0AYQY_zzD2-OlpSHeDxnWqFVEhXl446SyT_pA/edit",
                },
            ),
            Document(
                page_content="This approach is\npopularly known as a bag-of-words approach in natural language\nprocessing literature. The reason it is called\nbag-of-words is because it just gives about if and how\nmany times a word occurs. It doesn't care\nabout the position or order of the word\nin the sentence. Bag-of-words based language\nmodeling approaches have been the mainstay of language modeling\nfor a long time, and give comparative\nperformance on several natural language\nprocessing tasks were ordering information\nis not very important. However, they can\nperform poorly on tasks where ordering\ninformation is important.",
                metadata={
                    "source": "01_sequence-modeling.en.txt",
                    "course_number": "SIADS 642",
                    "course_title": "Deep Learning I",
                    "start_index": 2446,
                },
            ),
            Document(
                page_content="Cool.",
                metadata={
                    "source": "04_using-inkscape-to-trace-and-modify-visualizations.en.txt",
                    "course_number": "SIADS 523",
                    "course_title": "Communicating Data Science Results",
                    "start_index": 13476,
                },
            ),
            Document(
                page_content="",
                metadata={
                    "source": "05_university-of-michigans-primary-data-center.en.txt",
                    "course_number": "SIADS 673",
                    "course_title": "Cloud Computing",
                    "start_index": 0,
                },
            ),
            Document(
                page_content="So I'll give you an example\nthat comes to mind. You need to find labels for images. You are trying to find\ninstances of a backpack or you're trying to do facial detection. And so your thought might be okay, well,\ngive me 1000 images of people's faces or 10,000 peoples images of people's faces,\nlabel them. And we'll build a model to do that, and yes, you can do that, but\nwhy when you have the cloud. When we go into Amazon's\nmachine learning tab, there's a lot of different\nservices within here. And we're going to go through\na lot of these together. Some of these are fun services. Some of these are just really cool. For example, deep racer,\ndeep racer is the coolest thing, the coolest service from\nAmazon that I've seen. You get to race a car with machine\nlearning and you actually, where is it? You actually buy this car? This is a thing they sell on Amazon,\nlike the actual Amazon.com. You buy this car, it's a little kit,\nyou put together, it interfaces with Amazon's cloud. And you can build a model around\nracing on this and it's Amazon. So they're saying,\nhey you're charged for the storage, that's going to be S3 training and\nevaluation. That's going to be compute. And this is $3.50 an hour and\nmodel storage is 23 cents, I'm sorry,\ntwo cents per gigabyte per month. And you can actually go and buy this and\ncompete in Amazon services. There's not really like a business\nvalue specifically to this tool set. That's not entirely true.",
                metadata={
                    "source": "06_machine-learning-in-the-cloud.en.txt",
                    "course_number": "SIADS 673",
                    "course_title": "Cloud Computing",
                    "start_index": 942,
                },
            ),
        ],
    },
    #
    # Who are the instructors for the Capstone?
    {
        "query": "Who are the instructors for the Capstone?",
        "result": "1. Winston Featherly-Bean\n    2. Elle O'Brien\n    3. Michelle LeBlanc\n    4. Laura Stagnaro\n    5. Kyle Balog\n    6. Rachael Tatman\n    Detailed Answer:\n    The instructors for the Capstone are as follows:\n    1. Winston Featherly-Bean - Instructor\n    2. Elle O'Brien - Lead Instructor\n    3. Michelle LeBlanc - Instructor\n    4. Laura Stagnaro - Instructor\n    5. Kyle Balog - Instructor\n    6. Rachael Tatman - Instructor\n    These instructors will be responsible for providing guidance, support, and feedback to students throughout the Capstone project. They will also be involved in the assessment of student projects and the determination of final grades.",
        "source_documents": [
            Document(
                page_content="Capstone (SIADS 699), Instructor And Course Assistants: - Instructors: Winston Featherly-Bean, Elle O'Brien, Michelle LeBlanc, Laura Stagnaro, Kyle Balog and Rachael Tatman\n- Course manager: Kirtana Choragudi",
                metadata={
                    "source": "699_2023-10.md",
                    "heading": "Instructor And Course Assistants",
                    "section": "2",
                    "course_number": "SIADS 699",
                    "course_title": "Capstone",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/699%20.pdf",
                },
            ),
            Document(
                page_content="Hi, welcome to the capstone. My name's Dr. Elle O'brian\nand I'm going to be the lead instructor for your capstone of\nthe MADS program. The objective of this capstone is that you're going to\nbe working to create portfolio worthy projects\nthat demonstrate mastery of the Data\nScience skills that you've learned so\nfar in the curriculum, as well as depth of knowledge in a particular subject area. This is your opportunity\nto announce that you've arrived essentially in the data science community\nof professionals. You are going to\nhave the chance to test some of the skills that\nyou've developed so far, as well as to push yourself in ways that you might not have\ngotten the chance to yet, but are really interested in. You can start to develop some of your own personal brand by\npursuing your interests, and take these opportunities to challenge yourself by going further than you\npreviously have. I'm going to give a little\nbit of an overview of the course and just some of\nthe logistics around this. First of all, you've\nprobably already noticed that you'll be\nworking in teams of three. In the real-world, a lot of data science doesn't\nhappen independently, almost everything is going\nto involve some teamwork. Even if you're the sole\ndata scientist on the team, you'll often be working\nwith the data engineer, possibly someone on a front end, as well as people in\nbusiness analytics or whatever the application\nof your project is. Some domain experts and\nworking with others is actually one of the\ncore challenges of real-world applied\ndata science, it is not as easy as it seems. This is going to be your\nchance to confront some of those problems in\na setting that is somewhat emulative of\nwhat you might encounter in the real-world with\nall of the code sharing, project management,\nheadaches, and glories that that contains. In this class, we are going\nto have weekly office hours, instructors will be offering\nregular office hours. Office hours are not required\nor expected of you and we will not be having any planned reviews or\ncurriculum in them, office hours are for coming by and getting yourself unstuck. If you find yourself unable to move past part of your project, that's a good idea then, to come and talk to me or another instructor and we\ncan help you get unstuck.",
                metadata={
                    "source": "01_capstone-overview.en.txt",
                    "course_number": "SIADS 699",
                    "course_title": "Capstone",
                    "start_index": 0,
                },
            ),
            Document(
                page_content="Capstone (SIADS 699), Course Syllabus For SIADS 699 Course Overview and Prerequisites: The Capstone is a project-based course in which students propose and build end-to-end data science projects in their domains of interest. Students are asked to demonstrate mastery of data science concepts and methods from their MADS training and produce a creative, original, and technically rigorous portfolio piece. Projects will be supervised by instructors with regular peer review. The core of this class is a group data science project which will be independently designed and executed by students. The intention is to create a resume-worthy portfolio project in a format that is ready to share and present with the broader community of data science professionals.\n\nThe following are prerequisites for Capstone 699:\n\n- SIADS 694 & 695: Milestone II A and B\n- 1 data science application course (currently, these are SIADS 682: Social Media Analytics, SIADS 680: Learning Analytics, SIADS 685: Search and Recommender Systems, and SIADS 688: Data Science for Social Good)",
                metadata={
                    "source": "699_2023-10.md",
                    "heading": "Course Syllabus For SIADS 699 Course Overview and Prerequisites",
                    "section": "1",
                    "course_number": "SIADS 699",
                    "course_title": "Capstone",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/699%20.pdf",
                },
            ),
            Document(
                page_content="Capstone (SIADS 699), Letter Grades and Course Grades: Refer to the MADS Assignment Submission and Grading Policies section of the UMSI Student Handbook (access to Student Orientation course required). The grading scale for this course is as follows- note that an A+ can only be awarded at the discretion of the instructors . An A+ is a mark of a truly distinguished final project, and they are rare.\n\n|     |     |\n| --- | --- |\n| A   | 90% |\n| B+  | 87% |\n| B   | 80% |\n| C+  | 77% |\n| C   | 70% |\n| D+  | 67% |\n| D   | 60% |\n| F   |     |",
                metadata={
                    "source": "699_2023-10.md",
                    "heading": "Letter Grades and Course Grades",
                    "section": "11",
                    "course_number": "SIADS 699",
                    "course_title": "Capstone",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/699%20.pdf",
                },
            ),
            Document(
                page_content="Capstone (SIADS 699), Course Schedule All Times Are In Ann Arbor Time (Eastern Time).: - This course begins on September 26 and ends on December 18, 2023\n- Project proposals are due October 16 by 11:59 PM. This is the end of Week 3. - Group video standups should be posted in Slack by 11:59 pm (Ann Arbor, Michigan time - Eastern Time) by the following days:.\n  - Tuesday, October 24 by 11:59 PM (the first day of week 5 )\n  - Tuesday, November 7 by 11:59 PM (the first day of week 7 )\n  - Tuesday, November 28 by 11:59 PM (the first day of week 10 )\n- Students are required to respond to 2 other teams about their standups by the end of the standup week (the following Monday at midnight EST).\n- Teams must schedule a check-in meeting with their designated contact on the teaching team between October 31 and November 13 (during weeks 6 and 7).\n- Projects must be submitted to the instructional team by December 11, 2023 at 11:59 pm . Note this is one week before the official last day of class!",
                metadata={
                    "source": "699_2023-10.md",
                    "heading": "Course Schedule All Times Are In Ann Arbor Time (Eastern Time).",
                    "section": "7",
                    "course_number": "SIADS 699",
                    "course_title": "Capstone",
                    "course_date": "October 2023",
                    "document": "https://www.si.umich.edu/sites/default/files/699%20.pdf",
                },
            ),
        ],
    },
    #
    # Tell me a bit about PCA
    {
        "query": "Tell me a bit about PCA",
        "result": "1. Principal Component Analysis (PCA) is a statistical procedure used for dimensionality reduction. It's a way to simplify complex data by reducing the number of dimensions while retaining most of the information.\n    2. The main idea behind PCA is to find new orthogonal coordinate systems, called principal components, that can be used to represent the original data in a more compact and simpler form.\n    3. In terms of how it works mathematically, PCA involves finding the eigenvectors and eigenvalues of the covariance matrix of the original data. The eigenvectors correspond to the directions of the principal components, while the eigenvalues represent the amount of variance explained by each principal component.\n    4. Once you have identified the principal components and their corresponding eigenvalues, you can use these new coordinate systems to transform the original data into a lower-dimensional representation while retaining most of the information.\n    5. It's important to note that PCA is not always the best choice for dimensionality reduction depending on the specific characteristics of the data. For example, if the data has a nonlinear structure or if there are outliers or missing values in the data, then other more advanced techniques such as t-SNE, autoencoders, or deep learning may be more suitable for effectively reducing the dimensionality of the data while preserving its underlying structure and relationships.\n    6. In summary, PCA is a powerful statistical technique used for dimensionality reduction that involves finding new orthogonal coordinate systems called principal components that can be used to represent the original data in a more compact and simpler form while retaining most of the information. It's important to note that PCA may not always be the best choice for dimensionality reduction depending on the specific characteristics of the data, and other more advanced techniques such as t-SNE, autoencoders, or deep learning may be more suitable for effectively reducing the dimensionality of the data while preserving its underlying structure and relationships.",
        "source_documents": [
            Document(
                page_content="Well, I know that PCA sounds a little\nbit complex in terms of mathematics. But if you want to do PCA in Python,\nit is actually extremely easy./ All you need to do\nis to load the sklearn package and then you load the class\nof PCA decomposition. All you need to do is to use\nthe following two lines of code.",
                metadata={
                    "source": "04_3-3-4-principal-component-analysis.en.txt",
                    "course_number": "SIADS 532",
                    "course_title": "Data Mining I",
                    "start_index": 5478,
                },
            ),
            Document(
                page_content="There is a package called PCA in Python\nthat you can install and use if you like. It includes a biplot plotting routine\nwhich I've shown here on the right, very easy to install and use,\nalthough I haven't used it myself, some aspects of it are a little bit\nmore difficult to sort of customize. What I would recommend is just using\nthe notebook code that we provided, it's kind of instructive just to\ngo through it to see how it works. And then you feel free to use that code to\ncreate your own biplots for your datasets.",
                metadata={
                    "source": "05_pca-biplots-and-how-to-use-them.en.txt",
                    "course_number": "SIADS 543",
                    "course_title": "Unsupervised Learning",
                    "start_index": 19336,
                },
            ),
            Document(
                page_content="The new data will have fewer\ndimensions from the old data. So to summarize PCA, we know that principal components\nare very special patterns of matrix data. And in fact, they're orthogonal\neigenvectors of the covariance matrix. They are very useful because\nthey can define new orthogonal coordinate system of your matrix. And based on this orthogonal\ncoordinate system, many of the vector similarity or\ndistance matrix are much more trustable. Through PCA,\nyou can transform the original vector data into low dimensional and\northogonal vector space. And this is why PCA has been a very\nuseful step of feature engineering in many machine learning tasks. Is this it? In reality, shouldn't we always use PCA? And in fact,\nPCA also have some of its limitations. Why? Remember that PCA relies heavily\non eigenvalues and eigenvectors. And we know that eigenvalues and eigenvectors only apply\nto square matrices. Also PCA relies on eigendecomposition. And we know that stable eigendecomposition\ndoes not apply to all square matrices. In fact, it requires that\nyour matrix is symmetric and sometimes positive semi-definite. And that is why we apply PCA\nto the covariance matrix XTX, because we know that the covariance\nmatrix is symmetric and it is also positive semi-definite. But in reality, we know that the original data matrices\nwe deal with are almost never square.",
                metadata={
                    "source": "04_3-3-4-principal-component-analysis.en.txt",
                    "course_number": "SIADS 532",
                    "course_title": "Data Mining I",
                    "start_index": 5971,
                },
            ),
            Document(
                page_content="Let's start by looking at a very important and widely used linear dimensionality\nreduction technique called principal component\nanalysis or PCA. There are a couple of ways\nto describe how PCA works. An intuitive, more geometric way and then there's\na linear algebra way. What we're going\nto do is to start, we're going to look\nat the geometric way, the visually intuitive\nway and then later, we'll look at the\nlinear algebra behind PCA as part of understanding a powerful general\ndimensionality reduction method called singular value\ndecomposition or SVD, which is very closely\nconnected to PCA. Intuitively what PCA does, it takes your\noriginal data points. Here I have a very simple\ndataset with two features. It's a two-dimensional\ndataset and imagine each instance is denoted by a point here in the\nscatterplot and intuitively, what PCA does geometrically to these original data points\nis it finds a rotation of the points so that the\ndimensions are statistically uncorrelated and\nafter it does that, each data point can be\ndescribed by new coordinates relative to this new frame of reference in these\nuncorrelated dimensions. Once we find these new\nrotated dimensions, the nature of PCA is such that we can drop all but\nthe most informative coordinates that capture\nmost of the variation in the original dataset and\nwe still end up with a good approximation in the least square sense\nto our original dataset. Looking at this\nsynthetic example, we have two features\nthat are somewhat highly correlated and when we apply PCA. PCA will find the direction in the data has highest variance. What that means is, if we think\nabout PCA trying to find, there are different ways\nthat you can project this data onto a line. Imagine there are all\nthese different ways.",
                metadata={
                    "source": "03_intro-to-dimensionality-reduction-and-principal-components-analysis.en.txt",
                    "course_number": "SIADS 543",
                    "course_title": "Unsupervised Learning",
                    "start_index": 14870,
                },
            ),
            Document(
                page_content="I've actually been\nwarned about this, but I think it happens anyway. When I was working on this,\nAm I the Asshole dataset, there was one point\nwhere I was like, \"Wow. My model's really working. I'm getting amazing results.\" It was like 85 percent, and it had never been higher\nthan 68 percent accuracy. Then I realized that I had a leakage that I didn't intend, and it was that I had done\nPCA, and then splits. In PCA, before you split your data into\ntraining and test, then we'll incorporate\nlots of information about the tests set\ninto its features. What is PCA? Principal Components Analysis. It's a way of futurizing\nyour dataset. It's also a way to reduce\nthe dimensions of it. If you have tons and tons\nof dimensions in your data, and you don't think all of\nthem are that interesting. You think a lot of them are quite correlated with one another. There's really no reason to\nkeep 20 correlated features. You really only need one. You just can project it\ninto a lower dimension, and you sacrifice a\nlittle interpretability. But it's a great go-to, when you think you have a lot of correlations in your data. But if you do it before\nyou split your dataset, it's going to incorporate information about your test set, and that is bad. That will inflate what you\nthink your model can do.",
                metadata={
                    "source": "03_interview-with-elle-o-brien-of-dvc-org.en.txt",
                    "course_number": "SIADS 643",
                    "course_title": "Machine Learning Pipelines",
                    "start_index": 8892,
                },
            ),
        ],
    },
    #
    #
    # {
    #     "query": "Who is the instructor for the SQL and Databases class?",
    #     "result": "Graham Hukill (gshukill@umich.edu)",
    #     "source_documents": [
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
    #             metadata={
    #                 "source": "511_2023-10.md",
    #                 "heading": "Student Services",
    #                 "section": "17",
    #                 "course_number": "SIADS 511",
    #                 "course_title": "SQL and Databases",
    #                 "course_date": "October 2023",
    #                 "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
    #             },
    #         ),
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Mental Health: Refer to the University's Resources for Stress and Mental Health website for a listing of resources for students.",
    #             metadata={
    #                 "source": "511_2023-10.md",
    #                 "heading": "Student Mental Health",
    #                 "section": "16",
    #                 "course_number": "SIADS 511",
    #                 "course_title": "SQL and Databases",
    #                 "course_date": "October 2023",
    #                 "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
    #             },
    #         ),
    #     ],
    # },
    # {
    #     "query": "What classes does Graham Hukill teach?",
    #     "result": "Graham Hukill teaches Database Architecture & Technology (SIADS 611) and SQL and Databases (SIADS 511).",
    #     "source_documents": [
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
    #             metadata={
    #                 "source": "511_2023-10.md",
    #                 "heading": "Student Services",
    #                 "section": "17",
    #                 "course_number": "SIADS 511",
    #                 "course_title": "SQL and Databases",
    #                 "course_date": "October 2023",
    #                 "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
    #             },
    #         ),
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Mental Health: Refer to the University's Resources for Stress and Mental Health website for a listing of resources for students.",
    #             metadata={
    #                 "source": "511_2023-10.md",
    #                 "heading": "Student Mental Health",
    #                 "section": "16",
    #                 "course_number": "SIADS 511",
    #                 "course_title": "SQL and Databases",
    #                 "course_date": "October 2023",
    #                 "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
    #             },
    #         ),
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Course Outcomes: 1. Learn the SQL Language\n2. Learn relational database design\n3. Learn how to load and normalize data in databases\n4. Learn how to add indexes for performance\n5. Learn about stored procedures\n6. Learn Regular Expressions for scanning, parsing, and extracting data",
    #             metadata={
    #                 "source": "511_2023-10.md",
    #                 "heading": "Course Outcomes",
    #                 "section": "7",
    #                 "course_number": "SIADS 511",
    #                 "course_title": "SQL and Databases",
    #                 "course_date": "October 2023",
    #                 "document": "https://www.si.umich.edu/sites/default/files/511%20_0.pdf",
    #             },
    #         ),
    #     ],
    # },
    # {
    #     "query": "How many credits do I need to complete the MADS program?",
    #     "result": "You need to complete a minimum of 34 credit hours of SIADS coursework to earn a Master of Applied Data Science degree at the University of Michigan School of Information.",
    #     "source_documents": [
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
    #             metadata={
    #                 "source": "advising_guide.md",
    #                 "heading": "Graduation > Q: When should I apply for graduation?",
    #                 "section": "48",
    #                 "course_number": "n/a",
    #                 "course_title": "n/a",
    #                 "course_date": "n/a",
    #                 "document": "https://docs.google.com/document/d/1A3zdTF0AYQY_zzD2-OlpSHeDxnWqFVEhXl446SyT_pA/edit",
    #             },
    #         ),
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
    #             metadata={
    #                 "source": "handbook.md",
    #                 "heading": "MADS Slack Policy, Standards, and Practices > MADS Slack Standards and Processes > Use of Slack",
    #                 "section": "55",
    #                 "course_number": "n/a",
    #                 "course_title": "n/a",
    #                 "course_date": "n/a",
    #                 "document": "https://docs.google.com/document/d/1YEOcpdONdme5kmpNEnZpdbJeVFhEIw1pS0wq16QdH1I/edit",
    #             },
    #         ),
    #     ],
    # },
    # {
    #     "query": "How does PCA work?",
    #     "result": "PCA (Principal Component Analysis) is a statistical procedure...",
    #     "source_documents": [
    #         Document(
    #             page_content="SQL and Databases (SIADS 511), Student Services: Refer to the Introduction to UMSI Student Life section of the UMSI Student Handbook (access to the Student Orientation course required).",
    #             metadata={
    #                 "source": "06_machine-learning-in-the-cloud.en.txt",
    #                 "course_number": "SIADS 673",
    #                 "course_title": "Cloud Computing",
    #                 "start_index": 942,
    #             },
    #         ),
    #     ],
    # },
    # #
]
