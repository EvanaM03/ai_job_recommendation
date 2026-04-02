from django.core.management.base import BaseCommand
from django.utils.text import slugify
from skill.models import Skill
from jobs.models import Job, JobCategory
from company.models import Company


class Command(BaseCommand):
    help = 'Seeds database with sample skills, categories, companies, and jobs'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding skills...')
        skills_data = [
            ('Python', 'Programming'), ('JavaScript', 'Programming'), ('React', 'Frontend'),
            ('Django', 'Backend'), ('Node.js', 'Backend'), ('TypeScript', 'Programming'),
            ('SQL', 'Database'), ('PostgreSQL', 'Database'), ('MongoDB', 'Database'),
            ('Machine Learning', 'AI/ML'), ('Deep Learning', 'AI/ML'), ('Data Science', 'AI/ML'),
            ('TensorFlow', 'AI/ML'), ('PyTorch', 'AI/ML'), ('scikit-learn', 'AI/ML'),
            ('AWS', 'Cloud'), ('Azure', 'Cloud'), ('GCP', 'Cloud'),
            ('Docker', 'DevOps'), ('Kubernetes', 'DevOps'), ('Git', 'Tools'),
            ('HTML/CSS', 'Frontend'), ('Vue.js', 'Frontend'), ('Angular', 'Frontend'),
            ('Java', 'Programming'), ('C++', 'Programming'), ('Go', 'Programming'),
            ('REST APIs', 'Backend'), ('GraphQL', 'Backend'), ('Microservices', 'Architecture'),
            ('Agile', 'Methodology'), ('Scrum', 'Methodology'), ('UI/UX Design', 'Design'),
            ('Figma', 'Design'), ('Linux', 'Systems'), ('Cybersecurity', 'Security'),
            ('Data Analysis', 'Analytics'), ('Tableau', 'Analytics'), ('Excel', 'Analytics'),
            ('Communication', 'Soft Skills'), ('Leadership', 'Soft Skills'), ('Project Management', 'Management'),
        ]
        skill_objects = {}
        for name, category in skills_data:
            skill, created = Skill.objects.get_or_create(name=name, defaults={'category': category})
            skill_objects[name] = skill
            if created:
                self.stdout.write(f'  Created skill: {name}')

        self.stdout.write('Seeding job categories...')
        categories_data = [
            'Software Engineering', 'Data Science & AI', 'Product Management',
            'Design & UX', 'DevOps & Cloud', 'Marketing', 'Finance', 'Sales',
        ]
        cat_objects = {}
        for name in categories_data:
            cat, created = JobCategory.objects.get_or_create(
                name=name, defaults={'slug': slugify(name)}
            )
            cat_objects[name] = cat
            if created:
                self.stdout.write(f'  Created category: {name}')

        self.stdout.write('Seeding companies...')
        companies_data = [
            ('TechCorp Inc.', 'hire@techcorp.com', 'San Francisco, CA', 'https://techcorp.example.com'),
            ('DataVision Labs', 'careers@datavision.com', 'New York, NY', 'https://datavision.example.com'),
            ('CloudNative Solutions', 'jobs@cloudnative.com', 'Austin, TX', 'https://cloudnative.example.com'),
            ('DesignHub Studio', 'talent@designhub.com', 'Remote', 'https://designhub.example.com'),
            ('Fintech Dynamics', 'hr@fintechdyn.com', 'Chicago, IL', 'https://fintechdyn.example.com'),
        ]
        company_objects = {}
        for name, email, location, website in companies_data:
            company, created = Company.objects.get_or_create(
                name=name,
                defaults={'email': email, 'location': location, 'website': website,
                          'description': f'{name} is a leading company in its industry.'}
            )
            company_objects[name] = company

        self.stdout.write('Seeding jobs...')
        jobs_data = [
            {
                'title': 'Senior Python Developer',
                'company': 'TechCorp Inc.',
                'description': 'We are looking for a Senior Python Developer to build and maintain scalable web applications. You will work with Django, REST APIs, and cloud infrastructure. Strong experience with Python, Django, PostgreSQL, and AWS is required. You will collaborate with cross-functional teams to design and implement new features.',
                'location': 'San Francisco, CA',
                'salary_range': '$120,000 - $150,000',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['Python', 'Django', 'PostgreSQL', 'REST APIs', 'AWS'],
                'experience': 5,
            },
            {
                'title': 'Machine Learning Engineer',
                'company': 'DataVision Labs',
                'description': 'Join our AI team to build production machine learning systems. You will design and implement ML pipelines, work with large datasets, and deploy models to production. Experience with Python, TensorFlow, PyTorch, and data science is essential. You will work closely with data scientists to turn research into scalable systems.',
                'location': 'New York, NY',
                'salary_range': '$130,000 - $170,000',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Python', 'Machine Learning', 'TensorFlow', 'PyTorch', 'scikit-learn', 'SQL'],
                'experience': 3,
            },
            {
                'title': 'Full Stack JavaScript Developer',
                'company': 'TechCorp Inc.',
                'description': 'Build modern web applications using React and Node.js. You will work on both frontend and backend, creating responsive UIs and robust APIs. Knowledge of TypeScript, React, Node.js, MongoDB, and REST APIs is required. Great opportunity to work in a fast-paced startup environment.',
                'location': 'Remote',
                'salary_range': '$90,000 - $120,000',
                'job_type': 'Remote',
                'category': 'Software Engineering',
                'skills': ['JavaScript', 'React', 'Node.js', 'TypeScript', 'MongoDB'],
                'experience': 3,
            },
            {
                'title': 'Data Scientist',
                'company': 'DataVision Labs',
                'description': 'Analyze complex datasets to generate business insights. You will build predictive models, create data visualizations, and communicate findings to stakeholders. Strong skills in Python, machine learning, data analysis, SQL, and Tableau are needed. PhD or Masters in a quantitative field is preferred.',
                'location': 'New York, NY',
                'salary_range': '$110,000 - $140,000',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Python', 'Machine Learning', 'Data Science', 'SQL', 'Data Analysis', 'Tableau'],
                'experience': 2,
            },
            {
                'title': 'DevOps Engineer',
                'company': 'CloudNative Solutions',
                'description': 'Manage and improve our cloud infrastructure. You will work with AWS, Kubernetes, Docker, and CI/CD pipelines to ensure reliability and scalability. Strong knowledge of Linux, DevOps practices, and cloud platforms is required. You will help the engineering team ship faster and more reliably.',
                'location': 'Austin, TX',
                'salary_range': '$115,000 - $145,000',
                'job_type': 'Full-time',
                'category': 'DevOps & Cloud',
                'skills': ['Docker', 'Kubernetes', 'AWS', 'Linux', 'Git'],
                'experience': 4,
            },
            {
                'title': 'React Frontend Developer',
                'company': 'DesignHub Studio',
                'description': 'Create beautiful, responsive user interfaces using React and TypeScript. You will collaborate with designers to implement pixel-perfect UIs and ensure great user experiences. Proficiency in React, JavaScript, TypeScript, HTML/CSS, and Figma is expected. You will work in a creative environment with talented designers.',
                'location': 'Remote',
                'salary_range': '$85,000 - $110,000',
                'job_type': 'Remote',
                'category': 'Software Engineering',
                'skills': ['React', 'JavaScript', 'TypeScript', 'HTML/CSS'],
                'experience': 2,
            },
            {
                'title': 'UI/UX Designer',
                'company': 'DesignHub Studio',
                'description': 'Design intuitive and engaging user experiences for web and mobile products. You will conduct user research, create wireframes, prototypes, and high-fidelity designs. Mastery of Figma and strong UI/UX design skills are required. You will work directly with product managers and developers to bring designs to life.',
                'location': 'Remote',
                'salary_range': '$80,000 - $105,000',
                'job_type': 'Remote',
                'category': 'Design & UX',
                'skills': ['UI/UX Design', 'Figma'],
                'experience': 2,
            },
            {
                'title': 'Backend Java Developer',
                'company': 'Fintech Dynamics',
                'description': 'Develop and maintain high-performance financial systems using Java and microservices architecture. You will design APIs, work with databases, and ensure system reliability. Experience in Java, microservices, SQL, REST APIs, and cloud platforms is required. Financial domain knowledge is a plus.',
                'location': 'Chicago, IL',
                'salary_range': '$100,000 - $130,000',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['Java', 'Microservices', 'SQL', 'REST APIs', 'Docker'],
                'experience': 4,
            },
            {
                'title': 'Cloud Solutions Architect',
                'company': 'CloudNative Solutions',
                'description': 'Design and implement cloud architecture solutions on AWS and Azure. You will work with clients to assess their needs, design architectures, and oversee implementation. Deep expertise in AWS, Azure, Kubernetes, Docker, and microservices is required. Strong communication and leadership skills are essential.',
                'location': 'Austin, TX',
                'salary_range': '$150,000 - $190,000',
                'job_type': 'Full-time',
                'category': 'DevOps & Cloud',
                'skills': ['AWS', 'Azure', 'Kubernetes', 'Docker', 'Microservices', 'Leadership'],
                'experience': 7,
            },
            {
                'title': 'Data Engineer',
                'company': 'DataVision Labs',
                'description': 'Build and maintain scalable data pipelines and warehouses. You will work with large volumes of data, design ETL processes, and optimize query performance. Proficiency in Python, SQL, PostgreSQL, MongoDB, and cloud platforms is needed. You will enable the data science team to do their best work.',
                'location': 'New York, NY',
                'salary_range': '$105,000 - $135,000',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Python', 'SQL', 'PostgreSQL', 'MongoDB', 'AWS', 'Data Analysis'],
                'experience': 3,
            },
            {
                'title': 'Python ML Intern',
                'company': 'DataVision Labs',
                'description': 'Great opportunity for students to gain hands-on experience in machine learning and AI. You will assist the ML team in data preprocessing, model training, and evaluation. Knowledge of Python, scikit-learn, and data science fundamentals is helpful. Strong mathematical background and eagerness to learn are most important.',
                'location': 'New York, NY',
                'salary_range': '$25/hour',
                'job_type': 'Internship',
                'category': 'Data Science & AI',
                'skills': ['Python', 'scikit-learn', 'Data Analysis'],
                'experience': 0,
            },
            {
                'title': 'Product Manager - SaaS',
                'company': 'TechCorp Inc.',
                'description': 'Lead the product strategy and roadmap for our SaaS platform. You will work closely with engineering, design, and marketing teams to deliver high-impact features. Experience in product management, agile methodologies, and communication is required. Strong analytical and leadership skills are essential.',
                'location': 'San Francisco, CA',
                'salary_range': '$125,000 - $155,000',
                'job_type': 'Full-time',
                'category': 'Product Management',
                'skills': ['Agile', 'Scrum', 'Project Management', 'Communication', 'Leadership'],
                'experience': 5,
            },
        ]

        for job_data in jobs_data:
            if not Job.objects.filter(title=job_data['title'], company_name=job_data['company']).exists():
                company = company_objects.get(job_data['company'])
                category = cat_objects.get(job_data['category'])
                job = Job.objects.create(
                    title=job_data['title'],
                    company=company,
                    company_name=job_data['company'],
                    description=job_data['description'],
                    location=job_data['location'],
                    salary_range=job_data['salary_range'],
                    job_type=job_data['job_type'],
                    category=category,
                    required_experience=job_data['experience'],
                    status='Open',
                )
                for skill_name in job_data['skills']:
                    if skill_name in skill_objects:
                        job.required_skills.add(skill_objects[skill_name])
                self.stdout.write(f'  Created job: {job_data["title"]}')

        self.stdout.write(self.style.SUCCESS('Seed data created successfully!'))
