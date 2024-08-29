from django.shortcuts import render

def resume_view(request):
    context = {
        'name': 'Fariba Lotfi',
        'email': 'abiraf.lotfi@gmail.com',
        'phone': '+61452227409',
        'linkedin': 'https://www.linkedin.com/in/fariba-lotfi',
        'image': 'path_to_your_image.jpg',  # Place your image in the static folder

        'education': [
            'Ph.D. in Artificial Intelligence, Macquarie University & Sharif University of Technology, 2018 - 2024',
            'M.Sc. in Artificial Intelligence, Sharif University of Technology, 2016 - 2018',
            'B.Sc. in Computer Hardware Engineering, Shahid Beheshti University, 2011 - 2016',
        ],

        'career': [
            'Data Science Expert, truuth Company, Sydney, Australia, 2022 - Present',
            'IT Engineer, BAM Engineering Development Group, 2018',
            'Operating Systems (Debian) Lab Instructor, Sharif University of Technology, 2017 and 2019',
            'English Language Instructor, Elite Language School, 2016 - 2021',
            'Website Designer Intern, Parax Company, 2014',
        ],

        'awards': [
            'Excellence in Industry-Engaged Research, Centre for Applied Artificial Intelligence, Macquarie University, 2023',
            '1st place in the AI-Enabled Health Hackathon, 2023',
            'Best Paper Award in The 3rd International Workshop on AI-enabled Process Automation, 2022',
            '2nd Runner-up Award in The 2nd International Workshop on AI-enabled Process Automation, 2021',
        ],

        'certificates': [
            'AI in Healthcare Capstone, Stanford University, 2023',
            'Microsoft Azure Fundamentals AI-900, Microsoft, 2023',
            'AWS S3 Basics, Coursera, 2022',
            'Linux and Bash for Data Engineering, Duke University, 2022',
        ],

        'skills': [
            'Python, Bash Scripting, PostgreSQL, Java, Matlab, C/C++',
            'Machine Learning: PyTorch, TensorFlow, Keras, Scikit-Learn',
            'Data Visualization: Matplotlib, Seaborn, Plotly, Bokeh',
            'Cloud Computing: AWS S3, SageMaker, Kinesis',
        ],

        'publications': [
            'Lotfi, F., Beheshti, A., Jamzad, M., et al. (2024). Image-Based Enhancement of Document Classification and Segmentation. (Submitted to AAAI-25)',
            'Lotfi, F., Jamzad, M., Beigy, H., et al. (2024). Knowledge Graph Construction in Hyperbolic Space for Automatic Image Annotation. (Submitted to Image and Vision Computing)',
            'Lotfi, F., Beheshti, A., et al. (2024). The Open Story Model (OSM): Transforming Big Data into Interactive Narratives. ICWS (Accepted)',
        ]
    }
    return render(request, 'home.html', context)
