from django.core.management.base import BaseCommand
from django.utils.text import slugify
from skill.models import Skill
from jobs.models import Job, JobCategory
from company.models import Company


class Command(BaseCommand):
    help = 'Seeds database with Nepal-specific job data'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing jobs, companies, categories before seeding')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Job.objects.all().delete()
            Company.objects.all().delete()
            JobCategory.objects.all().delete()
            self.stdout.write('  Cleared jobs, companies, and categories.')

        # ── Skills ──────────────────────────────────────────────────────────
        self.stdout.write('Seeding skills...')
        skills_data = [
            ('Python', 'Programming'), ('JavaScript', 'Programming'), ('PHP', 'Programming'),
            ('Java', 'Programming'), ('C++', 'Programming'), ('C#', 'Programming'),
            ('Go', 'Programming'), ('TypeScript', 'Programming'), ('Kotlin', 'Programming'),
            ('React', 'Frontend'), ('Vue.js', 'Frontend'), ('Angular', 'Frontend'),
            ('HTML/CSS', 'Frontend'), ('Bootstrap', 'Frontend'), ('Next.js', 'Frontend'),
            ('Django', 'Backend'), ('Laravel', 'Backend'), ('Node.js', 'Backend'),
            ('Spring Boot', 'Backend'), ('REST APIs', 'Backend'), ('GraphQL', 'Backend'),
            ('Microservices', 'Architecture'), ('Flask', 'Backend'),
            ('MySQL', 'Database'), ('PostgreSQL', 'Database'), ('MongoDB', 'Database'),
            ('SQL', 'Database'), ('Redis', 'Database'), ('Oracle', 'Database'),
            ('Machine Learning', 'AI/ML'), ('Deep Learning', 'AI/ML'), ('Data Science', 'AI/ML'),
            ('TensorFlow', 'AI/ML'), ('PyTorch', 'AI/ML'), ('scikit-learn', 'AI/ML'),
            ('NLP', 'AI/ML'), ('Computer Vision', 'AI/ML'), ('Data Analysis', 'Analytics'),
            ('Tableau', 'Analytics'), ('Power BI', 'Analytics'), ('Excel', 'Analytics'),
            ('AWS', 'Cloud'), ('Azure', 'Cloud'), ('GCP', 'Cloud'),
            ('Docker', 'DevOps'), ('Kubernetes', 'DevOps'), ('Git', 'Tools'),
            ('Linux', 'Systems'), ('CI/CD', 'DevOps'), ('Jenkins', 'DevOps'),
            ('UI/UX Design', 'Design'), ('Figma', 'Design'), ('Adobe XD', 'Design'),
            ('Photoshop', 'Design'), ('Illustrator', 'Design'),
            ('Android Development', 'Mobile'), ('iOS Development', 'Mobile'),
            ('React Native', 'Mobile'), ('Flutter', 'Mobile'),
            ('Digital Marketing', 'Marketing'), ('SEO', 'Marketing'), ('Content Writing', 'Marketing'),
            ('Social Media Marketing', 'Marketing'), ('Google Ads', 'Marketing'),
            ('Accounting', 'Finance'), ('Tally', 'Finance'), ('Financial Analysis', 'Finance'),
            ('QuickBooks', 'Finance'), ('Auditing', 'Finance'),
            ('Network Administration', 'Networking'), ('Cybersecurity', 'Security'),
            ('Ethical Hacking', 'Security'), ('Cisco', 'Networking'),
            ('Agile', 'Methodology'), ('Scrum', 'Methodology'), ('Project Management', 'Management'),
            ('Communication', 'Soft Skills'), ('Leadership', 'Soft Skills'), ('Teamwork', 'Soft Skills'),
            ('Customer Support', 'Service'), ('Technical Writing', 'Documentation'),
        ]
        skill_objects = {}
        for name, category in skills_data:
            skill, created = Skill.objects.get_or_create(name=name, defaults={'category': category})
            skill_objects[name] = skill
            if created:
                self.stdout.write(f'  + Skill: {name}')

        # ── Categories ───────────────────────────────────────────────────────
        self.stdout.write('Seeding categories...')
        categories_data = [
            'Software Engineering', 'Data Science & AI', 'Mobile Development',
            'Design & UX', 'DevOps & Cloud', 'Digital Marketing',
            'Finance & Accounting', 'IT Support & Networking',
            'Product Management', 'Cybersecurity', 'Content & Writing',
        ]
        cat_objects = {}
        for name in categories_data:
            cat, _ = JobCategory.objects.get_or_create(name=name, defaults={'slug': slugify(name)})
            cat_objects[name] = cat
        self.stdout.write(f'  {len(cat_objects)} categories ready.')

        # ── Nepal Companies ──────────────────────────────────────────────────
        self.stdout.write('Seeding Nepal companies...')
        companies_data = [
            ('Leapfrog Technology',     'careers@lftechnology.com',  'Kathmandu, Nepal',  'https://lftechnology.com',
             'Leapfrog Technology is a leading software development company based in Kathmandu, building world-class digital products for global clients.'),
            ('F1Soft International',    'hr@f1soft.com',             'Kathmandu, Nepal',  'https://f1soft.com',
             'F1Soft is Nepal\'s largest fintech company, powering digital payment solutions like eSewa and Fonepay.'),
            ('Fusemachines Nepal',      'jobs@fusemachines.com',     'Kathmandu, Nepal',  'https://fusemachines.com',
             'Fusemachines is an AI company democratizing artificial intelligence talent and solutions across Nepal and the world.'),
            ('Cotiviti Nepal',          'recruit@cotiviti.com',      'Lalitpur, Nepal',   'https://cotiviti.com',
             'Cotiviti Nepal provides healthcare analytics and technology solutions, employing hundreds of IT professionals in Lalitpur.'),
            ('Deerwalk Services',       'careers@deerwalk.com',      'Kathmandu, Nepal',  'https://deerwalk.com',
             'Deerwalk provides healthcare IT services and data analytics solutions, with a large engineering team in Kathmandu.'),
            ('CloudFactory Nepal',      'talent@cloudfactory.com',   'Kathmandu, Nepal',  'https://cloudfactory.com',
             'CloudFactory connects a skilled global workforce to process data for AI and machine learning pipelines.'),
            ('Bajra Technologies',      'hr@bajratechnologies.com',  'Kathmandu, Nepal',  'https://bajratechnologies.com',
             'Bajra Technologies is a digital agency delivering software, mobile apps, and digital marketing services.'),
            ('Yomari Information',      'careers@yomari.com',        'Kathmandu, Nepal',  'https://yomari.com',
             'Yomari provides IT consulting, custom software, and cloud services to enterprises across Nepal.'),
            ('Vianet Communications',   'jobs@vianet.com.np',        'Kathmandu, Nepal',  'https://vianet.com.np',
             'Vianet is one of Nepal\'s top internet service providers, also offering cloud and managed IT services.'),
            ('Genese Solution',         'hr@genesesolution.com',     'Kathmandu, Nepal',  'https://genesesolution.com',
             'Genese Solution is an AWS Premier Partner providing cloud consulting and training services in Nepal.'),
            ('Verisk Nepal',            'careers@verisk.com',        'Lalitpur, Nepal',   'https://verisk.com',
             'Verisk Nepal is the South Asia division of Verisk Analytics, focused on data analytics for the insurance industry.'),
            ('IntroCept Nepal',         'hr@introcept.com',          'Kathmandu, Nepal',  'https://introcept.com',
             'IntroCept Nepal is a software company specializing in open-source solutions, enterprise software, and mobile apps.'),
            ('Sparrow SMS',             'jobs@sparrowsms.com',       'Kathmandu, Nepal',  'https://sparrowsms.com',
             'Sparrow SMS provides bulk SMS, digital marketing, and communication API solutions across Nepal.'),
            ('Ncell Pvt. Ltd.',         'careers@ncell.com.np',      'Kathmandu, Nepal',  'https://ncell.com.np',
             'Ncell is Nepal\'s largest mobile network operator, serving millions of subscribers with 4G/LTE services.'),
            ('Nepal Telecom',           'hr@ntc.net.np',             'Kathmandu, Nepal',  'https://ntc.net.np',
             'Nepal Telecom (NTC) is the national telecom provider offering voice, data, and broadband services.'),
            ('Danphe Inc.',             'careers@danphe.com',        'Kathmandu, Nepal',  'https://danphe.com',
             'Danphe is a healthcare technology company building hospital management software for Nepal and South Asia.'),
            ('Daraz Nepal',             'jobs@daraz.com.np',         'Kathmandu, Nepal',  'https://daraz.com.np',
             'Daraz is Nepal\'s leading e-commerce marketplace, part of the Alibaba Group, connecting buyers and sellers nationwide.'),
            ('Foodmandu',               'hr@foodmandu.com',          'Kathmandu, Nepal',  'https://foodmandu.com',
             'Foodmandu is Nepal\'s pioneer food delivery platform, connecting restaurants and customers across the Kathmandu Valley.'),
            ('Himalayan Bank',          'careers@himalayanbank.com', 'Kathmandu, Nepal',  'https://himalayanbank.com',
             'Himalayan Bank is one of Nepal\'s premier commercial banks, offering full banking and digital financial services.'),
            ('Sastodeal',               'jobs@sastodeal.com',        'Kathmandu, Nepal',  'https://sastodeal.com',
             'Sastodeal is Nepal\'s fastest growing e-commerce and deals platform with a strong technology and marketing team.'),
        ]
        company_objects = {}
        for name, email, location, website, desc in companies_data:
            company, _ = Company.objects.get_or_create(
                name=name, defaults={'email': email, 'location': location, 'website': website, 'description': desc}
            )
            company_objects[name] = company
        self.stdout.write(f'  {len(company_objects)} companies ready.')

        # ── Nepal Jobs ───────────────────────────────────────────────────────
        self.stdout.write('Seeding Nepal jobs...')
        jobs_data = [
            # ── SOFTWARE ENGINEERING ────────────────────────────────────────
            {
                'title': 'Senior Software Engineer (Python/Django)',
                'company': 'Leapfrog Technology',
                'description': 'Leapfrog Technology is hiring a Senior Software Engineer to lead development of complex web applications for international clients. You will architect scalable backend systems using Python and Django, design REST APIs, and integrate with cloud infrastructure on AWS. You are expected to mentor junior engineers, conduct code reviews, and collaborate closely with cross-functional agile teams. Strong understanding of software design patterns, PostgreSQL, Docker, and CI/CD pipelines is required. 5+ years of professional experience in Python development is mandatory.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 80,000 - 1,20,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['Python', 'Django', 'PostgreSQL', 'REST APIs', 'AWS', 'Docker', 'Git'],
                'experience': 5,
            },
            {
                'title': 'Full Stack Developer (React + Node.js)',
                'company': 'Bajra Technologies',
                'description': 'Bajra Technologies is looking for a skilled Full Stack Developer to build modern web applications for clients across various industries. You will develop responsive frontends with React and TypeScript, build Node.js backend services, and integrate REST APIs and databases. You should be comfortable working in an agile environment, writing clean maintainable code, and participating in technical discussions. Knowledge of MongoDB, Git, and deployment workflows is expected. This is a great opportunity to grow in a collaborative digital agency.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 60,000 - 90,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['React', 'Node.js', 'JavaScript', 'TypeScript', 'MongoDB', 'REST APIs', 'Git'],
                'experience': 3,
            },
            {
                'title': 'PHP Laravel Developer',
                'company': 'IntroCept Nepal',
                'description': 'IntroCept Nepal seeks a PHP Laravel Developer to work on enterprise web applications and open-source CMS platforms. You will build RESTful APIs, develop reusable backend components, and maintain MySQL databases. Experience with Laravel framework, MVC architecture, jQuery, and Git is required. Familiarity with Linux server environments and deployment is a plus. You will work in a team of experienced engineers focused on code quality and best practices.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 50,000 - 80,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['PHP', 'Laravel', 'MySQL', 'REST APIs', 'JavaScript', 'Git', 'Linux'],
                'experience': 2,
            },
            {
                'title': 'Java Backend Developer',
                'company': 'Cotiviti Nepal',
                'description': 'Cotiviti Nepal is looking for a Java Backend Developer to work on healthcare data analytics platforms used by major insurance companies in the US. You will develop scalable microservices using Spring Boot, integrate with Oracle databases, and write comprehensive unit tests. Experience with Java, Spring Boot, RESTful APIs, SQL, and agile development is required. Exposure to healthcare IT standards (HL7, FHIR) is a plus. This role offers excellent career growth in a large multinational organization.',
                'location': 'Lalitpur, Nepal',
                'salary_range': 'NPR 70,000 - 1,10,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['Java', 'Spring Boot', 'Oracle', 'Microservices', 'REST APIs', 'SQL', 'Agile'],
                'experience': 3,
            },
            {
                'title': '.NET / C# Developer',
                'company': 'Yomari Information',
                'description': 'Yomari Information Services is hiring a .NET Developer to build enterprise-grade business applications and ERP integrations for corporate clients in Nepal. You will develop and maintain C# applications, design MS SQL databases, and build APIs that integrate with existing business systems. Experience with .NET framework, C#, SQL Server, REST APIs, and entity framework is essential. Good communication skills and the ability to gather requirements from clients is important. This role comes with attractive benefits and career advancement.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 55,000 - 85,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['C#', 'SQL', 'REST APIs', 'JavaScript', 'Git'],
                'experience': 2,
            },
            {
                'title': 'Junior Software Developer',
                'company': 'Sparrow SMS',
                'description': 'Sparrow SMS is hiring a Junior Software Developer to join our growing product team. You will assist in developing and maintaining our SMS gateway, bulk messaging platform, and marketing APIs. The role involves writing clean PHP or Python code, working with MySQL databases, and supporting backend API integrations. Freshers with strong programming fundamentals are encouraged to apply. You will be mentored by senior developers and get hands-on experience shipping real products used by thousands of businesses in Nepal.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 30,000 - 50,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['PHP', 'Python', 'MySQL', 'REST APIs', 'Git', 'HTML/CSS'],
                'experience': 0,
            },
            {
                'title': 'Frontend Developer (React)',
                'company': 'Daraz Nepal',
                'description': 'Daraz Nepal is looking for a Frontend Developer to build and optimize our e-commerce platform\'s user interfaces. You will work with React, Next.js, and TypeScript to create fast, accessible, and visually appealing components. Collaborating with product managers and backend engineers, you will implement new features, improve page performance, and ensure cross-browser compatibility. Experience with React, JavaScript, HTML/CSS, Git, and RESTful API integration is required. Strong attention to detail and a passion for excellent user experience is a must.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 65,000 - 95,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['React', 'Next.js', 'TypeScript', 'JavaScript', 'HTML/CSS', 'Git'],
                'experience': 2,
            },
            {
                'title': 'Software Engineer – Healthcare IT',
                'company': 'Danphe Inc.',
                'description': 'Danphe Inc. is looking for a Software Engineer to enhance its hospital management system used by hospitals across Nepal and South Asia. You will develop new modules in C# and Angular, work with SQL Server databases, and integrate with HL7 lab and pharmacy systems. Attention to detail, understanding of healthcare workflows, and clean code practices are important. Experience with C#, Angular, SQL, and REST APIs is required. This is a meaningful role impacting patient care in hundreds of hospitals.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 60,000 - 90,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['C#', 'Angular', 'SQL', 'REST APIs', 'Git'],
                'experience': 2,
            },
            {
                'title': 'Backend Developer (Go/Golang)',
                'company': 'Leapfrog Technology',
                'description': 'Leapfrog Technology is seeking a Go developer to build high-performance backend services for global SaaS products. You will design and implement microservices in Go, integrate with PostgreSQL and Redis, deploy on AWS, and write high-quality tests. Experience with Go, PostgreSQL, Docker, REST APIs, and cloud deployments is required. Familiarity with gRPC and message queues (Kafka/RabbitMQ) is a plus. You will work in a global team with engineers across Nepal and the US.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 90,000 - 1,40,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['Go', 'PostgreSQL', 'Docker', 'REST APIs', 'Microservices', 'AWS', 'Redis'],
                'experience': 3,
            },
            {
                'title': 'Software Engineering Intern',
                'company': 'Fusemachines Nepal',
                'description': 'Fusemachines Nepal offers a 3-month software engineering internship for students and recent graduates passionate about building AI-powered applications. Interns will assist developers in building features using Python, React, and REST APIs, participate in agile ceremonies, and learn best practices in software development. Strong programming skills in any language, eagerness to learn, and good communication are essential. This internship often leads to full-time employment. A monthly stipend will be provided.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 15,000 - 25,000/month',
                'job_type': 'Internship',
                'category': 'Software Engineering',
                'skills': ['Python', 'JavaScript', 'HTML/CSS', 'Git', 'Communication'],
                'experience': 0,
            },
            # ── DATA SCIENCE & AI ────────────────────────────────────────────
            {
                'title': 'AI/ML Engineer',
                'company': 'Fusemachines Nepal',
                'description': 'Fusemachines Nepal is hiring an AI/ML Engineer to develop and deploy machine learning models for clients across various industries. You will build NLP and computer vision pipelines, train and fine-tune deep learning models using TensorFlow and PyTorch, and deploy them to cloud infrastructure. Experience with Python, machine learning, deep learning, and data science is essential. Familiarity with MLOps practices, Docker, and AWS is a plus. You will work alongside world-class AI researchers and contribute to cutting-edge AI projects.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 85,000 - 1,30,000/month',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Python', 'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'NLP', 'AWS'],
                'experience': 2,
            },
            {
                'title': 'Data Scientist',
                'company': 'Verisk Nepal',
                'description': 'Verisk Nepal is looking for a Data Scientist to analyze large insurance and risk datasets and develop predictive models for the US insurance market. You will build statistical and machine learning models, perform data exploration and feature engineering, and present insights to stakeholders. Strong skills in Python, scikit-learn, SQL, and data visualization are required. Experience with actuarial data, R, or insurance domain knowledge is a significant advantage. Excellent salary and international exposure await.',
                'location': 'Lalitpur, Nepal',
                'salary_range': 'NPR 1,00,000 - 1,50,000/month',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Python', 'Machine Learning', 'Data Science', 'scikit-learn', 'SQL', 'Data Analysis'],
                'experience': 3,
            },
            {
                'title': 'Data Analyst',
                'company': 'Deerwalk Services',
                'description': 'Deerwalk Services is seeking a Data Analyst to work on healthcare claims data for US health plans. You will query large datasets, build dashboards, and generate reports that help clients understand their member populations and manage costs. Proficiency in SQL, Python or R, Excel, and data visualization tools (Tableau or Power BI) is required. Healthcare industry knowledge is a plus. This role offers strong career growth opportunities within a large, established data services company.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 55,000 - 80,000/month',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['SQL', 'Python', 'Data Analysis', 'Tableau', 'Power BI', 'Excel'],
                'experience': 1,
            },
            {
                'title': 'Data Annotation Specialist',
                'company': 'CloudFactory Nepal',
                'description': 'CloudFactory Nepal is hiring Data Annotation Specialists to label and validate training datasets for AI and machine learning models. You will annotate images, text, audio, and video data following detailed guidelines, perform quality checks, and maintain high accuracy standards. Strong attention to detail, consistency, and ability to follow instructions are key. No prior technical experience required — full training provided. Flexible part-time and full-time options are available.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 25,000 - 40,000/month',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['Data Analysis', 'Communication', 'Teamwork', 'Excel'],
                'experience': 0,
            },
            {
                'title': 'Business Intelligence Developer',
                'company': 'Cotiviti Nepal',
                'description': 'Cotiviti Nepal is looking for a BI Developer to build and maintain analytics dashboards and reporting pipelines for healthcare clients. You will design SSRS and Power BI reports, write complex SQL queries, and work with data warehousing concepts. Experience with SQL, Power BI, SSRS, ETL processes, and data modelling is required. Exposure to Azure Data Factory and Databricks is a plus. You will collaborate with US-based analytics teams to deliver high-quality business intelligence solutions.',
                'location': 'Lalitpur, Nepal',
                'salary_range': 'NPR 75,000 - 1,10,000/month',
                'job_type': 'Full-time',
                'category': 'Data Science & AI',
                'skills': ['SQL', 'Power BI', 'Data Analysis', 'Python', 'Azure', 'Excel'],
                'experience': 3,
            },
            # ── MOBILE DEVELOPMENT ───────────────────────────────────────────
            {
                'title': 'Android Developer (Kotlin)',
                'company': 'F1Soft International',
                'description': 'F1Soft International is hiring an Android Developer to work on eSewa and Fonepay mobile applications used by millions of users across Nepal. You will design and implement new features, improve app performance, and ensure a seamless payment experience for users. Proficiency in Kotlin, Android SDK, REST API integration, and Git is required. Knowledge of fintech, payment gateways, and security best practices is a strong advantage. Join Nepal\'s leading digital payments company.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 70,000 - 1,10,000/month',
                'job_type': 'Full-time',
                'category': 'Mobile Development',
                'skills': ['Android Development', 'Kotlin', 'REST APIs', 'Git', 'SQL'],
                'experience': 2,
            },
            {
                'title': 'Flutter Developer',
                'company': 'Bajra Technologies',
                'description': 'Bajra Technologies is seeking a Flutter Developer to build cross-platform mobile applications for clients in Nepal and internationally. You will develop pixel-perfect UIs using Flutter and Dart, integrate REST APIs, and publish apps to Google Play and the App Store. Experience with Flutter, Dart, REST APIs, Git, and state management solutions (Provider/Bloc) is required. Knowledge of Firebase integration and push notifications is a plus. A collaborative, learning-focused work environment awaits.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 55,000 - 85,000/month',
                'job_type': 'Full-time',
                'category': 'Mobile Development',
                'skills': ['Flutter', 'REST APIs', 'Git', 'Firebase', 'Android Development', 'iOS Development'],
                'experience': 2,
            },
            {
                'title': 'React Native Developer',
                'company': 'Daraz Nepal',
                'description': 'Daraz Nepal is looking for a React Native Developer to work on our mobile shopping app serving millions of users. You will build and improve app features, optimize performance, fix bugs, and integrate backend APIs. Experience with React Native, JavaScript, Redux, REST APIs, and debugging tools is required. Understanding of iOS and Android deployment processes is a plus. This is a high-impact role on one of Nepal\'s most-used consumer apps.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 65,000 - 1,00,000/month',
                'job_type': 'Full-time',
                'category': 'Mobile Development',
                'skills': ['React Native', 'JavaScript', 'REST APIs', 'Git', 'Android Development', 'iOS Development'],
                'experience': 2,
            },
            # ── DESIGN & UX ──────────────────────────────────────────────────
            {
                'title': 'UI/UX Designer',
                'company': 'Leapfrog Technology',
                'description': 'Leapfrog Technology is seeking a talented UI/UX Designer to create intuitive user experiences for web and mobile products delivered to global clients. You will conduct user research, create wireframes, design high-fidelity prototypes in Figma, and collaborate with developers throughout implementation. Strong proficiency in Figma, UI/UX Design principles, design systems, and user testing is required. Experience with motion design and accessibility standards is an advantage. Build products that reach millions of users worldwide.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 60,000 - 90,000/month',
                'job_type': 'Full-time',
                'category': 'Design & UX',
                'skills': ['UI/UX Design', 'Figma', 'Adobe XD', 'Communication', 'Teamwork'],
                'experience': 2,
            },
            {
                'title': 'Graphic Designer',
                'company': 'Daraz Nepal',
                'description': 'Daraz Nepal is hiring a Graphic Designer to create compelling visual content for campaigns, banners, social media, and the platform UI. You will produce high-quality graphics using Photoshop and Illustrator, collaborate with the marketing team on promotional materials, and ensure brand consistency. Proficiency in Photoshop, Illustrator, and Figma is required. Experience in e-commerce or retail marketing design is a bonus. A creative, fast-paced environment where your work is seen by millions.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 40,000 - 65,000/month',
                'job_type': 'Full-time',
                'category': 'Design & UX',
                'skills': ['Photoshop', 'Illustrator', 'Figma', 'UI/UX Design', 'Communication'],
                'experience': 1,
            },
            # ── DEVOPS & CLOUD ───────────────────────────────────────────────
            {
                'title': 'DevOps Engineer',
                'company': 'Genese Solution',
                'description': 'Genese Solution, Nepal\'s top AWS Partner, is hiring a DevOps Engineer to manage cloud infrastructure and CI/CD pipelines for clients. You will provision and manage AWS services, configure Kubernetes clusters, automate deployments using Jenkins and Terraform, and monitor system health. Strong knowledge of AWS, Docker, Kubernetes, Linux, CI/CD, and Infrastructure-as-Code is required. AWS certifications are highly valued. Join a team at the forefront of cloud adoption in Nepal.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 80,000 - 1,20,000/month',
                'job_type': 'Full-time',
                'category': 'DevOps & Cloud',
                'skills': ['AWS', 'Docker', 'Kubernetes', 'Linux', 'CI/CD', 'Jenkins', 'Git'],
                'experience': 3,
            },
            {
                'title': 'Cloud Support Engineer',
                'company': 'Genese Solution',
                'description': 'Genese Solution is looking for a Cloud Support Engineer to help clients migrate to and optimize their AWS cloud environments. You will troubleshoot cloud infrastructure issues, answer client queries, set up monitoring and alerting, and assist with cost optimization. Knowledge of AWS services (EC2, S3, RDS, Lambda), Linux, and networking fundamentals is required. AWS certifications are a strong plus. You will also assist in delivering AWS training workshops.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 50,000 - 80,000/month',
                'job_type': 'Full-time',
                'category': 'DevOps & Cloud',
                'skills': ['AWS', 'Linux', 'Docker', 'Git', 'Communication'],
                'experience': 1,
            },
            # ── DIGITAL MARKETING ────────────────────────────────────────────
            {
                'title': 'Digital Marketing Specialist',
                'company': 'Daraz Nepal',
                'description': 'Daraz Nepal is hiring a Digital Marketing Specialist to plan and execute performance marketing campaigns across Google, Facebook, Instagram, and TikTok. You will manage paid ad campaigns, analyze ROI, optimize for conversions, and collaborate with the creative team on ad content. Experience with Google Ads, Facebook Ads, SEO, Google Analytics, and digital marketing strategy is required. A data-driven mindset and ability to interpret campaign metrics is essential for success in this role.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 45,000 - 70,000/month',
                'job_type': 'Full-time',
                'category': 'Digital Marketing',
                'skills': ['Digital Marketing', 'Google Ads', 'SEO', 'Social Media Marketing', 'Data Analysis'],
                'experience': 2,
            },
            {
                'title': 'SEO & Content Strategist',
                'company': 'Sastodeal',
                'description': 'Sastodeal is looking for an SEO and Content Strategist to grow organic search traffic and improve content quality across the platform. You will conduct keyword research, optimize product and blog pages, write SEO-friendly content, and build backlinks. Proficiency in SEO tools (SEMrush, Ahrefs), content writing, Google Analytics, and on-page SEO is required. Understanding of e-commerce content strategies and a track record of improving search rankings is a big advantage.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 35,000 - 55,000/month',
                'job_type': 'Full-time',
                'category': 'Digital Marketing',
                'skills': ['SEO', 'Content Writing', 'Digital Marketing', 'Social Media Marketing', 'Communication'],
                'experience': 1,
            },
            {
                'title': 'Social Media Manager',
                'company': 'Foodmandu',
                'description': 'Foodmandu is seeking a creative Social Media Manager to manage our social media presence and community across Facebook, Instagram, and TikTok. You will create engaging content, run campaigns, respond to customer queries, analyze engagement metrics, and collaborate with the marketing team. Strong writing skills, creativity, and experience with social media marketing tools are required. Knowledge of photo/video editing and a passion for food culture are a bonus.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 30,000 - 50,000/month',
                'job_type': 'Full-time',
                'category': 'Digital Marketing',
                'skills': ['Social Media Marketing', 'Content Writing', 'Digital Marketing', 'Photoshop', 'Communication'],
                'experience': 1,
            },
            # ── FINANCE & ACCOUNTING ─────────────────────────────────────────
            {
                'title': 'Finance Officer',
                'company': 'Himalayan Bank',
                'description': 'Himalayan Bank is hiring a Finance Officer to support daily financial operations including accounts payable/receivable, bank reconciliations, and financial reporting. You will maintain accurate accounting records using Tally, prepare monthly reports, and ensure compliance with Nepal Rastra Bank regulations. A Bachelor\'s degree in Accounting or Finance, knowledge of Tally and Excel, and understanding of banking operations is required. CA/ACCA qualification is a strong advantage.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 40,000 - 65,000/month',
                'job_type': 'Full-time',
                'category': 'Finance & Accounting',
                'skills': ['Accounting', 'Tally', 'Financial Analysis', 'Excel', 'Communication'],
                'experience': 2,
            },
            {
                'title': 'Senior Accountant',
                'company': 'Ncell Pvt. Ltd.',
                'description': 'Ncell is hiring a Senior Accountant to manage financial reporting, tax compliance, and internal audits. You will prepare financial statements, oversee payroll processing, coordinate with auditors, and ensure compliance with local tax laws and IFRS standards. A Chartered Accountant (CA) qualification or equivalent, strong knowledge of Tally/SAP, auditing, and financial analysis is required. 4+ years of experience in accounting at a large organization is needed.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 70,000 - 1,00,000/month',
                'job_type': 'Full-time',
                'category': 'Finance & Accounting',
                'skills': ['Accounting', 'Auditing', 'Financial Analysis', 'Tally', 'Excel', 'Leadership'],
                'experience': 4,
            },
            # ── IT SUPPORT & NETWORKING ──────────────────────────────────────
            {
                'title': 'IT Support Engineer',
                'company': 'Vianet Communications',
                'description': 'Vianet Communications is hiring an IT Support Engineer to provide technical assistance to enterprise clients and manage internal IT infrastructure. You will troubleshoot hardware and software issues, configure network equipment, manage Active Directory, and ensure IT systems remain operational. Knowledge of Windows Server, Linux, networking fundamentals, and hardware troubleshooting is required. Cisco CCNA certification is a strong plus. Must be comfortable with on-site visits across the Kathmandu Valley.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 35,000 - 55,000/month',
                'job_type': 'Full-time',
                'category': 'IT Support & Networking',
                'skills': ['Network Administration', 'Linux', 'Cisco', 'Communication', 'Teamwork'],
                'experience': 1,
            },
            {
                'title': 'Network Engineer',
                'company': 'Nepal Telecom',
                'description': 'Nepal Telecom is hiring a Network Engineer to manage and optimize the national telecom backbone network infrastructure. You will configure and maintain routers, switches, and fiber optic systems, monitor network performance, and respond to outages. Strong knowledge of networking protocols (BGP, OSPF, MPLS), Cisco equipment, Linux, and network monitoring tools is required. A bachelor\'s degree in Computer Engineering or Electronics is expected. This is a prestigious role at Nepal\'s national telecom operator.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 55,000 - 85,000/month',
                'job_type': 'Full-time',
                'category': 'IT Support & Networking',
                'skills': ['Network Administration', 'Cisco', 'Linux', 'Communication', 'Teamwork'],
                'experience': 3,
            },
            # ── CYBERSECURITY ────────────────────────────────────────────────
            {
                'title': 'Information Security Analyst',
                'company': 'F1Soft International',
                'description': 'F1Soft International is hiring an Information Security Analyst to protect the security of Nepal\'s largest digital payment infrastructure. You will conduct vulnerability assessments, monitor for security incidents, perform penetration testing, and ensure PCI-DSS compliance. Experience in cybersecurity, ethical hacking, network security, and security incident response is required. CEH, OSCP, or equivalent certification is highly valued. This is a critical role in protecting the financial data of millions of Nepali users.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 80,000 - 1,20,000/month',
                'job_type': 'Full-time',
                'category': 'Cybersecurity',
                'skills': ['Cybersecurity', 'Ethical Hacking', 'Network Administration', 'Linux', 'Python'],
                'experience': 3,
            },
            # ── PRODUCT MANAGEMENT ───────────────────────────────────────────
            {
                'title': 'Product Manager',
                'company': 'F1Soft International',
                'description': 'F1Soft International is looking for an experienced Product Manager to drive the product roadmap for its fintech platforms including eSewa. You will gather user requirements, prioritize features, write product specifications, and coordinate with engineering and design teams to deliver impactful releases. Strong experience in product management, agile methodologies, stakeholder communication, and data-driven decision-making is essential. Understanding of Nepal\'s digital payment landscape and prior fintech experience is a strong advantage.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 90,000 - 1,40,000/month',
                'job_type': 'Full-time',
                'category': 'Product Management',
                'skills': ['Agile', 'Scrum', 'Project Management', 'Communication', 'Leadership', 'Data Analysis'],
                'experience': 4,
            },
            # ── REMOTE / PART-TIME ───────────────────────────────────────────
            {
                'title': 'Remote Python Developer (Part-time)',
                'company': 'Leapfrog Technology',
                'description': 'Leapfrog Technology is looking for a part-time remote Python developer to assist with ongoing client projects. You will work approximately 20 hours per week on feature development, bug fixing, and code reviews. Strong Python skills, experience with Django or Flask, REST APIs, PostgreSQL, and Git are required. This role is ideal for experienced developers looking for flexible work arrangements while staying engaged with real product development.',
                'location': 'Remote, Nepal',
                'salary_range': 'NPR 40,000 - 60,000/month',
                'job_type': 'Part-time',
                'category': 'Software Engineering',
                'skills': ['Python', 'Django', 'Flask', 'REST APIs', 'PostgreSQL', 'Git'],
                'experience': 2,
            },
            {
                'title': 'Freelance UI/UX Designer',
                'company': 'Bajra Technologies',
                'description': 'Bajra Technologies regularly brings on freelance UI/UX designers for project-based work. You will design user interfaces for web and mobile apps, create Figma prototypes, and work directly with developers and project managers. Strong Figma skills, a solid portfolio, and the ability to work independently are required. Projects typically run 1–3 months. Great opportunity for experienced designers who want flexible work while building a strong project portfolio in Nepal\'s growing tech industry.',
                'location': 'Remote, Nepal',
                'salary_range': 'NPR 50,000 - 80,000/month',
                'job_type': 'Contract',
                'category': 'Design & UX',
                'skills': ['UI/UX Design', 'Figma', 'Adobe XD', 'Communication'],
                'experience': 2,
            },
            {
                'title': 'Content Writer (Tech)',
                'company': 'Genese Solution',
                'description': 'Genese Solution is hiring a Technical Content Writer to produce blog articles, cloud tutorials, AWS guides, and case studies. You will write clear, engaging technical content for both technical and non-technical audiences, collaborate with cloud engineers for accuracy, and optimize content for SEO. Strong writing skills, basic cloud/tech knowledge, and SEO familiarity are required. Prior technical writing experience or a degree in Computer Science or related field is preferred. Remote-friendly position.',
                'location': 'Kathmandu, Nepal',
                'salary_range': 'NPR 30,000 - 50,000/month',
                'job_type': 'Full-time',
                'category': 'Content & Writing',
                'skills': ['Content Writing', 'Technical Writing', 'SEO', 'Communication', 'AWS'],
                'experience': 1,
            },
            # ── POKHARA / OTHER CITIES ───────────────────────────────────────
            {
                'title': 'Web Developer',
                'company': 'Bajra Technologies',
                'description': 'Bajra Technologies is expanding to Pokhara and is hiring a Web Developer to serve clients in the Gandaki Province. You will build websites and small web applications using HTML/CSS, JavaScript, PHP, and MySQL. Ability to communicate with local clients, understand requirements, and deliver projects on time is key. Experience with WordPress, Laravel, and Bootstrap is a plus. This is a great opportunity to be part of Nepal\'s growing tech scene outside Kathmandu.',
                'location': 'Pokhara, Nepal',
                'salary_range': 'NPR 35,000 - 55,000/month',
                'job_type': 'Full-time',
                'category': 'Software Engineering',
                'skills': ['PHP', 'HTML/CSS', 'JavaScript', 'MySQL', 'Bootstrap', 'Git'],
                'experience': 1,
            },
            {
                'title': 'IT Officer',
                'company': 'Himalayan Bank',
                'description': 'Himalayan Bank is hiring an IT Officer for its Pokhara branch to manage IT operations, user support, and system maintenance. You will handle hardware/software troubleshooting, manage the branch LAN, liaise with head office IT for system upgrades, and train staff on IT tools. Knowledge of networking, Windows Server, and core banking software is required. A bachelor\'s degree in Computer Science or IT is expected. Good communication skills and a service-oriented attitude are essential.',
                'location': 'Pokhara, Nepal',
                'salary_range': 'NPR 40,000 - 60,000/month',
                'job_type': 'Full-time',
                'category': 'IT Support & Networking',
                'skills': ['Network Administration', 'Linux', 'Communication', 'Teamwork', 'Excel'],
                'experience': 1,
            },
        ]

        created_count = 0
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
                created_count += 1
                self.stdout.write(f'  + {job_data["title"]} @ {job_data["company"]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created_count} Nepal jobs seeded across {len(company_objects)} companies.'
        ))
