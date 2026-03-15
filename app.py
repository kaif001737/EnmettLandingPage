from datetime import datetime, timezone
import smtplib
from email.message import EmailMessage

from flask import Flask, jsonify, render_template, request

# Static configuration (inlined from .env)
FLASK_DEBUG = True  # equivalent to FLASK_ENV=development / FLASK_DEBUG=1
PORT = 5000
FLASK_HOST = "0.0.0.0"

MAIL_SERVER = "smtp.office365.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "contact@enmett.com"
MAIL_PASSWORD = "qrfhymnccgckjpxh"
MAIL_DEFAULT_SENDER = "contact@enmett.com"
MAIL_TO = "contact@enmett.com"
MAIL_SUPPRESS_SEND = False


app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/index.html")
def home_alias():
    return render_template("index.html")


@app.get("/services")
def services_main():
    return render_template("services.html")


SERVICES = {
    "sap-solutions": {
        "title": "SAP Solutions",
        "tagline": "End-to-end SAP solutions - from strategy to success.",
        "hero_title": "End-to-End SAP Solutions - From Strategy to Success",
        "hero_subtitle": (
            "Transform your business with scalable, secure, and intelligent SAP solutions delivered by Enmett experts."
        ),
        "hero_description": (
            "At Enmett, we provide complete SAP services-from strategic roadmap planning and implementation to optimization "
            "and long-term support. Our team helps organizations streamline operations, improve efficiency, and unlock the "
            "full potential of SAP technologies."
        ),
        "overview_title": "Complete SAP Services for Modern Enterprises",
        "overview": (
            "Enmett delivers comprehensive SAP solutions designed to help businesses accelerate digital transformation. "
            "Our services cover the entire SAP lifecycle-from consulting and planning to deployment, integration, and "
            "continuous optimization."
        ),
        "overview_more": (
            "We help organizations adopt the latest SAP technologies including SAP S/4HANA, SAP Business Technology Platform, "
            "SAP Analytics Cloud, and SAP integrations to create intelligent and connected business environments."
        ),
        "sap_services": [
            {
                "title": "SAP Consulting",
                "description": (
                    "We analyze your business processes and design a strategic SAP roadmap aligned with your organizational goals."
                ),
            },
            {
                "title": "SAP Implementation",
                "description": "Full lifecycle SAP implementation including system design, configuration, testing, and deployment.",
            },
            {
                "title": "SAP Migration",
                "description": "Seamless migration from legacy systems to SAP S/4HANA with minimal downtime and data integrity.",
            },
            {
                "title": "SAP Integration",
                "description": (
                    "Integrate SAP with third-party applications, cloud platforms, and enterprise systems for seamless workflows."
                ),
            },
            {
                "title": "SAP Custom Development",
                "description": "Custom SAP solutions tailored to your business needs using ABAP, Fiori, and SAP BTP technologies.",
            },
            {
                "title": "SAP Support & Maintenance",
                "description": (
                    "24/7 SAP support services to ensure system reliability, performance optimization, and continuous improvement."
                ),
            },
        ],
        "technologies": [
            "SAP S/4HANA",
            "SAP Fiori",
            "SAP Business Technology Platform (BTP)",
            "SAP Analytics Cloud",
            "SAP SuccessFactors",
            "SAP Ariba",
            "SAP Integration Suite",
            "SAP Data Migration Tools",
        ],
        "technologies_note": (
            "Our certified SAP specialists leverage modern SAP technologies to build intelligent enterprise solutions that scale "
            "with your business growth."
        ),
        "delivery_approach_title": "Our SAP Delivery Approach (Roadmap to Run)",
        "delivery_approach": [
            {
                "title": "Discover",
                "description": "Understanding business challenges, goals, and technical environment.",
            },
            {
                "title": "Plan",
                "description": "Create SAP roadmap, architecture design, and project strategy.",
            },
            {
                "title": "Implement",
                "description": "Configure SAP modules, develop custom features, and integrate systems.",
            },
            {
                "title": "Test",
                "description": "Ensure performance, security, and functionality through rigorous testing.",
            },
            {
                "title": "Deploy",
                "description": "Smooth SAP deployment with minimal business disruption.",
            },
            {
                "title": "Optimize & Support",
                "description": "Continuous monitoring, optimization, and long-term support services.",
            },
        ],
        "industries": [
            "Manufacturing",
            "Retail & E-commerce",
            "Healthcare",
            "Finance & Banking",
            "Logistics & Supply Chain",
            "Energy & Utilities",
        ],
        "industries_note": (
            "Our SAP solutions are tailored to meet the specific operational needs of different industries."
        ),
        "why_choose": [
            "Certified SAP Experts",
            "End-to-End Implementation Services",
            "Scalable Cloud-Based Solutions",
            "Secure Data Migration",
            "Faster Deployment",
            "24/7 Technical Support",
            "Cost-Effective Digital Transformation",
        ],
        "benefits": [
            "Improved Operational Efficiency",
            "Real-time Data Insights",
            "Automated Business Processes",
            "Better Decision Making",
            "Scalable Enterprise Systems",
        ],
        "case_study": {
            "title": "SAP Transformation for Retail Company",
            "description": (
                "We helped a retail enterprise migrate from legacy ERP to SAP S/4HANA, improving operational efficiency by 35% "
                "and enabling real-time analytics across departments."
            ),
        },
        "faqs": [
            {
                "q": "What SAP services does Enmett provide?",
                "a": "We provide consulting, implementation, migration, integration, and ongoing support for SAP systems.",
            },
            {
                "q": "How long does SAP implementation take?",
                "a": "Project timelines vary depending on business size and complexity, typically ranging from 3-12 months.",
            },
            {
                "q": "Do you support SAP S/4HANA migration?",
                "a": "Yes, we provide full migration services from legacy ERP systems to SAP S/4HANA.",
            },
        ],
        # Backward-compatible keys used by the generic service template.
        "capabilities": [
            "SAP consulting and roadmap planning",
            "Implementation, migration, and integration",
            "Custom development with ABAP, Fiori, and SAP BTP",
            "Optimization, support, and long-term maintenance",
        ],
        "value": [
            "Certified SAP experts across strategy, delivery, and run",
            "Secure migration and integration with minimal disruption",
            "Scalable solutions aligned to modern SAP best practices",
        ],
    },
    "cyber-security": {
        "title": "Cyber Security",
        "tagline": "Cyber security solutions for a secure digital future.",
        "hero_title": "Cyber Security Solutions for a Secure Digital Future",
        "hero_subtitle": (
            "Protect your business from evolving cyber threats with advanced security solutions from Enmett."
        ),
        "hero_description": (
            "Enmett provides comprehensive cyber security services designed to safeguard your digital assets, protect "
            "sensitive data, and ensure business continuity. Our security experts implement proactive strategies to "
            "detect, prevent, and respond to cyber threats."
        ),
        "overview_title": "Advanced Cyber Security for Modern Businesses",
        "overview": (
            "In today's digital world, cyber threats are constantly evolving. Enmett helps organizations strengthen their "
            "security posture with advanced cyber security solutions that protect networks, applications, and critical "
            "business data."
        ),
        "overview_more": (
            "Our security services focus on risk assessment, threat detection, vulnerability management, and incident "
            "response to ensure businesses stay secure and compliant."
        ),
        "security_services": [
            {
                "title": "Network Security",
                "description": (
                    "Protect corporate networks from unauthorized access, malware, and cyber attacks using advanced firewalls, "
                    "intrusion detection systems, and monitoring tools."
                ),
            },
            {
                "title": "Application Security",
                "description": (
                    "Identify and eliminate vulnerabilities in web and mobile applications to prevent exploitation and data breaches."
                ),
            },
            {
                "title": "Cloud Security",
                "description": "Secure cloud infrastructure and applications across AWS, Azure, and Google Cloud platforms.",
            },
            {
                "title": "Vulnerability Assessment & Penetration Testing (VAPT)",
                "description": "Identify security weaknesses through penetration testing and vulnerability scanning.",
            },
            {
                "title": "Identity & Access Management (IAM)",
                "description": (
                    "Ensure secure access control by implementing identity verification and user authentication systems."
                ),
            },
            {
                "title": "Security Monitoring & Incident Response",
                "description": "Continuous monitoring of systems to detect threats and respond quickly to cyber incidents.",
            },
        ],
        "technologies_title": "Cyber Security Technologies We Use",
        "technologies": [
            "Firewall & Network Protection Tools",
            "SIEM (Security Information and Event Management)",
            "Endpoint Protection Platforms",
            "Intrusion Detection Systems (IDS/IPS)",
            "Cloud Security Tools",
            "Multi-Factor Authentication (MFA)",
        ],
        "technologies_note": (
            "Our cyber security specialists leverage advanced technologies to create a strong security infrastructure for businesses."
        ),
        "tech_icon": "SEC",
        "delivery_approach_title": "Our Security Approach",
        "delivery_approach": [
            {
                "title": "Security Assessment",
                "description": "Analyze existing systems and identify vulnerabilities.",
            },
            {
                "title": "Risk Analysis",
                "description": "Evaluate potential threats and their impact on business operations.",
            },
            {
                "title": "Security Implementation",
                "description": "Deploy security frameworks, tools, and policies.",
            },
            {
                "title": "Monitoring & Detection",
                "description": "Continuously monitor systems for suspicious activities.",
            },
            {
                "title": "Incident Response",
                "description": "Quickly respond to security incidents and minimize damage.",
            },
            {
                "title": "Continuous Improvement",
                "description": "Regularly update security strategies to combat evolving cyber threats.",
            },
        ],
        "industries": [
            "Banking & Financial Services",
            "Healthcare",
            "E-commerce",
            "Government",
            "Manufacturing",
            "IT & Technology",
        ],
        "industries_note": (
            "Our cyber security solutions are tailored to meet the security requirements of various industries."
        ),
        "why_choose_title": "Why Choose Enmett for Cyber Security",
        "why_choose": [
            "Certified Cyber Security Experts",
            "Advanced Threat Detection Systems",
            "Proactive Security Monitoring",
            "Compliance with Security Standards",
            "24/7 Security Support",
            "Customized Security Strategies",
        ],
        "benefits_title": "Key Benefits",
        "benefits": [
            "Protection from Cyber Attacks",
            "Secure Data & Digital Assets",
            "Reduced Security Risks",
            "Compliance with Security Regulations",
            "Business Continuity & Trust",
        ],
        "case_study": {
            "title": "Cyber Security Upgrade for E-commerce Platform",
            "description": (
                "Enmett implemented advanced security measures for an online retail company, reducing cyber threats by 60% and "
                "strengthening customer data protection."
            ),
        },
        "faqs": [
            {
                "q": "What cyber security services does Enmett provide?",
                "a": (
                    "We provide network security, application security, cloud security, vulnerability testing, and incident response services."
                ),
            },
            {
                "q": "How often should businesses perform security testing?",
                "a": (
                    "Security testing should be performed regularly, ideally every 6-12 months or after major system updates."
                ),
            },
            {
                "q": "Do you provide cloud security solutions?",
                "a": "Yes, we secure cloud platforms such as AWS, Azure, and Google Cloud.",
            },
        ],
        # Backward-compatible keys used by the generic service template.
        "capabilities": [
            "Network, application, and cloud security services",
            "Vulnerability assessments and penetration testing (VAPT)",
            "Identity and access management (IAM) implementations",
            "Monitoring and incident response for critical systems",
        ],
        "value": [
            "Certified experts with practical, risk-based security delivery",
            "Advanced monitoring and faster response to evolving threats",
            "Security controls aligned to compliance and business continuity",
        ],
    },
    "it-managed-services": {
        "title": "IT Managed Services",
        "tagline": "Managed IT services for seamless business operations.",
        "hero_title": "Managed IT Services for Seamless Business Operations",
        "hero_subtitle": "Let Enmett manage your IT while you focus on growing your business.",
        "hero_description": (
            "Enmett’s IT Managed Services provide proactive monitoring, maintenance, and management of your IT infrastructure. "
            "Our team ensures your systems operate smoothly, securely, and efficiently with minimal downtime."
        ),
        "overview_title": "Proactive IT Management for Modern Organizations",
        "overview": (
            "Managing IT infrastructure can be complex and resource-intensive. Enmett’s Managed IT Services help businesses reduce "
            "operational costs, improve system reliability, and maintain secure technology environments."
        ),
        "overview_more": (
            "Our experts continuously monitor and manage your IT systems to ensure optimal performance and rapid issue resolution."
        ),
        "services_title": "Our Managed IT Services",
        "services_subtitle": "Always-on operations with proactive monitoring and structured support.",
        "managed_services": [
            {
                "title": "24/7 IT Monitoring",
                "description": (
                    "Continuous monitoring of IT infrastructure to detect and resolve issues before they impact business operations."
                ),
            },
            {
                "title": "Network Management",
                "description": "Management and optimization of network systems for reliable connectivity and performance.",
            },
            {
                "title": "IT Help Desk Support",
                "description": "Dedicated support team to assist users with technical issues and system troubleshooting.",
            },
            {
                "title": "Security Management",
                "description": (
                    "Implementation and monitoring of security measures to protect business systems from cyber threats."
                ),
            },
            {
                "title": "Data Backup & Disaster Recovery",
                "description": (
                    "Secure data backup solutions and recovery strategies to ensure business continuity."
                ),
            },
            {
                "title": "Patch Management & Updates",
                "description": "Regular updates and patch management to keep systems secure and up to date.",
            },
        ],
        "technologies_title": "Managed IT Technologies",
        "technologies": [
            "Remote Monitoring Tools",
            "Security Management Platforms",
            "Backup & Recovery Solutions",
            "Network Monitoring Systems",
            "Cloud Management Platforms",
        ],
        "technologies_note": (
            "We use proven monitoring and management platforms to keep your environments stable, secure, and continuously improved."
        ),
        "tech_icon": "MSP",
        "delivery_approach_title": "Our Managed IT Process",
        "delivery_approach": [
            {
                "title": "Assessment",
                "description": "Evaluate existing IT infrastructure.",
            },
            {
                "title": "Planning",
                "description": "Design a managed IT strategy.",
            },
            {
                "title": "Implementation",
                "description": "Deploy monitoring and management tools.",
            },
            {
                "title": "Monitoring",
                "description": "Continuous system monitoring and maintenance.",
            },
            {
                "title": "Optimization",
                "description": "Improve performance and security.",
            },
        ],
        "benefits_title": "Benefits of Managed IT Services",
        "benefits": [
            "Reduced IT Operational Costs",
            "24/7 System Monitoring",
            "Faster Issue Resolution",
            "Improved Cyber Security",
            "Scalable IT Infrastructure",
            "Increased Business Productivity",
        ],
        "why_choose_title": "Why Choose Enmett",
        "why_choose": [
            "Experienced Managed IT Experts",
            "Proactive IT Support",
            "Advanced Monitoring Systems",
            "Reliable Infrastructure Management",
            "Dedicated Customer Support",
        ],
        # Backward-compatible keys used by the generic service template.
        "capabilities": [
            "24/7 monitoring, help desk, and network management",
            "Security management and patching programs",
            "Backup, recovery, and continuity planning",
        ],
        "value": [
            "Predictable support with proactive monitoring and maintenance",
            "Faster resolution through defined processes and tooling",
            "Scalable coverage that grows with your business",
        ],
    },
    "resourcing": {
        "title": "Resourcing",
        "tagline": "Specialist talent to extend your own teams.",
        "overview": (
            "When you need additional SAP, security, or IT capacity, we provide experienced professionals who can join "
            "your projects or operations quickly."
        ),
        "capabilities": [
            "On‑site, near‑shore, and remote delivery models",
            "Individual experts or full scrum teams",
            "Short‑term backfill and long‑term augmentation",
        ],
        "value": [
            "Access to vetted specialists with deep domain experience",
            "Flexible commercial models for project or run‑mode work",
            "Capability uplift for your internal teams over time",
        ],
    },
    "ai-automation": {
        "title": "AI & Automation",
        "tagline": "AI and automation solutions for intelligent enterprises.",
        "hero_title": "AI & Automation Solutions for Intelligent Enterprises",
        "hero_subtitle": (
            "Driving smarter decisions, optimized processes, and accelerated digital transformation."
        ),
        "hero_description": (
            "Enmett delivers advanced AI and Automation solutions that help organizations improve efficiency, "
            "reduce operational costs, and unlock new business opportunities. By leveraging artificial intelligence, "
            "machine learning, and intelligent automation, we enable businesses to transform operations and achieve "
            "sustainable growth."
        ),
        "overview_title": "Intelligent Technologies for Modern Business",
        "overview": (
            "In today's competitive landscape, organizations must move beyond traditional processes and adopt "
            "intelligent technologies to remain agile and efficient. AI and automation are reshaping how businesses "
            "operate—enabling data-driven decision-making, predictive insights, and process optimization."
        ),
        "overview_more": (
            "At Enmett, we combine industry expertise with cutting-edge AI technologies to build intelligent systems "
            "that automate workflows, enhance productivity, and improve customer experiences. Our solutions are "
            "designed to integrate seamlessly with existing enterprise platforms such as SAP, cloud systems, and IT "
            "infrastructure."
        ),
        "services_title": "Our AI & Automation Services",
        "services_subtitle": "End-to-end AI and automation capabilities across strategy, implementation, and optimization.",
        "ai_automation_services": [
            {
                "title": "Artificial Intelligence Solutions",
                "description": (
                    "We develop AI-powered systems that analyze data, identify patterns, and generate actionable "
                    "insights to support business strategy and operational efficiency."
                ),
            },
            {
                "title": "Machine Learning Models",
                "description": (
                    "Our machine learning solutions help organizations predict trends, detect anomalies, and optimize "
                    "decision-making processes using advanced data analysis."
                ),
            },
            {
                "title": "Intelligent Process Automation (IPA)",
                "description": (
                    "We automate repetitive and manual processes to improve accuracy, reduce errors, and increase "
                    "operational speed."
                ),
            },
            {
                "title": "Robotic Process Automation (RPA)",
                "description": (
                    "Our RPA solutions streamline business workflows by automating rule-based tasks across "
                    "enterprise systems."
                ),
            },
            {
                "title": "AI-Powered Analytics",
                "description": (
                    "We implement advanced analytics platforms that provide real-time insights, forecasting "
                    "capabilities, and performance monitoring."
                ),
            },
            {
                "title": "AI Integration with Enterprise Systems",
                "description": (
                    "Enmett integrates AI solutions with SAP, ERP, CRM, and cloud platforms to create intelligent "
                    "and connected enterprise environments."
                ),
            },
        ],
        "technologies_title": "Technology Capabilities",
        "technologies": [
            "Machine Learning & Deep Learning Frameworks",
            "Natural Language Processing (NLP)",
            "Robotic Process Automation Tools",
            "Cloud AI Platforms",
            "Data Analytics & Business Intelligence",
            "Enterprise System Integration (SAP, ERP, CRM)",
        ],
        "technologies_note": (
            "Our AI and automation solutions leverage modern technologies to build intelligent, scalable systems "
            "that integrate with your existing enterprise landscape."
        ),
        "tech_icon": "AI",
        "delivery_approach_title": "Our Approach",
        "delivery_approach": [
            {
                "title": "Assessment",
                "description": "We analyze business processes to identify automation and AI opportunities.",
            },
            {
                "title": "Strategy & Design",
                "description": "Develop a tailored AI and automation roadmap aligned with business objectives.",
            },
            {
                "title": "Implementation",
                "description": "Deploy intelligent solutions integrated with enterprise systems.",
            },
            {
                "title": "Optimization",
                "description": "Continuously monitor and refine AI models for improved performance.",
            },
        ],
        "industries": [
            "Manufacturing",
            "Finance & Banking",
            "Healthcare",
            "Retail & E-commerce",
            "Logistics & Supply Chain",
            "Technology",
        ],
        "industries_note": (
            "Our AI and automation solutions are tailored to meet the operational needs of various industries."
        ),
        "why_choose_title": "Why Choose Enmett for AI & Automation",
        "why_choose": [
            "Industry Expertise with Cutting-Edge AI",
            "Seamless Enterprise Integration",
            "End-to-End Implementation Support",
            "Scalable and Future-Ready Solutions",
            "Proven Automation Frameworks",
        ],
        "benefits_title": "Benefits of AI & Automation",
        "benefits": [
            "Increased operational efficiency",
            "Reduced manual workload and operational costs",
            "Improved decision-making through predictive insights",
            "Faster and more accurate business processes",
            "Enhanced customer experiences",
            "Scalable and future-ready technology systems",
        ],
        "case_study": {
            "title": "AI-Powered Process Automation for Manufacturing",
            "description": (
                "Enmett implemented intelligent process automation for a manufacturing client, reducing manual "
                "data entry by 70% and improving order processing accuracy while enabling real-time analytics."
            ),
        },
        "faqs": [
            {
                "q": "What AI and automation services does Enmett provide?",
                "a": (
                    "We provide AI solutions, machine learning models, IPA, RPA, AI-powered analytics, and "
                    "enterprise system integration."
                ),
            },
            {
                "q": "How does AI integrate with SAP and ERP systems?",
                "a": (
                    "We integrate AI solutions with SAP, ERP, CRM, and cloud platforms to create intelligent, "
                    "connected enterprise environments."
                ),
            },
            {
                "q": "What is the typical timeline for AI and automation implementation?",
                "a": (
                    "Timelines vary based on scope and complexity, typically ranging from a few weeks for RPA "
                    "to several months for full AI and IPA implementations."
                ),
            },
        ],
        "capabilities": [
            "AI solutions, machine learning, IPA, and RPA",
            "AI-powered analytics and enterprise integration",
            "Assessment, strategy, implementation, and optimization",
        ],
        "value": [
            "Intelligent systems that automate workflows and enhance productivity",
            "Seamless integration with SAP, ERP, CRM, and cloud platforms",
            "Scalable solutions aligned to business objectives and growth",
        ],
    },
}


@app.get("/services/<slug>")
def service_detail(slug: str):
    service = SERVICES.get(slug)
    if not service:
        return render_template("services.html"), 404
    return render_template("service_detail.html", service=service, slug=slug)


INDUSTRIES = {
    "finance": {
        "title": "Finance",
        "tagline": "Helping financial institutions deliver secure, efficient, and customer-centric services.",
        "overview": (
            "The financial services industry is undergoing rapid digital transformation driven by changing customer "
            "expectations, regulatory requirements, and emerging technologies. Enmett helps financial institutions "
            "modernize their systems, optimize operations, and deliver secure digital financial services. "
            "Our solutions enable organizations to improve risk management, enhance security, and gain real-time "
            "insights into financial data."
        ),
        "initiatives": [
            "Digital banking solutions and modern customer platforms",
            "Financial data analytics and real-time insights",
            "Cyber security for financial systems and fraud prevention",
            "Payment system integration for banks and fintechs",
            "Regulatory compliance and reporting solutions",
        ],
    },
    "retail": {
        "title": "Retail",
        "tagline": "Empowering retailers with innovative technology to enhance customer engagement and business growth.",
        "overview": (
            "The retail industry is rapidly evolving with the growth of e-commerce, digital payments, and data-driven "
            "customer engagement. Enmett helps retailers leverage modern technologies to optimize supply chains, "
            "improve customer experiences, and streamline business operations."
        ),
        "initiatives": [
            "E-commerce technology solutions for scalable, secure online platforms",
            "Retail analytics for customer behavior and sales insights",
            "Supply chain optimization and inventory visibility",
            "Customer experience solutions and personalization",
            "Retail cyber security for systems and customer data",
        ],
    },
    "hospitality": {
        "title": "Hospitality",
        "tagline": "Enhancing guest experiences through innovative digital solutions.",
        "overview": (
            "The hospitality industry depends heavily on exceptional customer experiences and operational efficiency. "
            "Enmett helps hotels, resorts, and hospitality businesses leverage modern technology to improve guest "
            "services, optimize operations, and enhance overall customer satisfaction."
        ),
        "initiatives": [
            "Hotel management systems for reservations and operations",
            "Customer experience platforms and personalized guest engagement",
            "Hospitality analytics for behavior and performance insights",
            "Secure payment systems for hospitality businesses",
            "Reliable IT infrastructure for hotels and hospitality organizations",
        ],
    },
    "manufacturing": {
        "title": "Manufacturing",
        "tagline": "Driving efficiency and innovation in modern manufacturing operations.",
        "overview": (
            "Manufacturers are adopting advanced technologies to improve production efficiency, reduce costs, and "
            "increase operational visibility. Enmett provides digital solutions that help manufacturers optimize "
            "supply chains, automate production processes, and enhance overall operational performance."
        ),
        "initiatives": [
            "Smart factory solutions for automated, optimized production",
            "Supply chain management systems for better visibility",
            "Data analytics for real-time production optimization",
            "ERP & SAP solutions for end-to-end operations management",
            "Industrial cyber security for manufacturing systems",
        ],
    },
    "oil-gas": {
        "title": "Oil & Gas",
        "tagline": "Digital transformation for safe, efficient oil & gas operations.",
        "overview": (
            "The oil and gas industry faces complex operational challenges, including resource management, regulatory "
            "compliance, and operational efficiency. Enmett provides technology solutions that help energy companies "
            "optimize operations, improve safety, and enhance decision-making through advanced data insights."
        ),
        "initiatives": [
            "Energy data analytics for production monitoring and optimization",
            "Operational technology integration for efficient field operations",
            "Asset management systems for critical infrastructure",
            "Cyber security for energy systems and industrial control environments",
            "Supply chain and logistics solutions for energy operations",
        ],
    },
    "public-sector": {
        "title": "Public Sector",
        "tagline": "Supporting government organizations with innovative and secure technology solutions.",
        "overview": (
            "Government agencies and public sector organizations are increasingly adopting digital technologies to "
            "improve public services, increase transparency, and enhance operational efficiency. Enmett provides secure "
            "and scalable technology solutions that support digital transformation in the public sector."
        ),
        "initiatives": [
            "Government digital platforms for improved public service delivery",
            "Data management solutions for secure, efficient data handling",
            "Cyber security for government systems and citizen data",
            "Smart city technologies and modern infrastructure solutions",
            "IT infrastructure modernization for legacy government systems",
        ],
    },
}


@app.get("/industry")
def industry_main():
    return render_template("industry.html")


@app.get("/industry/<slug>")
def industry_detail(slug: str):
    industry = INDUSTRIES.get(slug)
    if not industry:
        return render_template("industry.html"), 404
    return render_template("industry_detail.html", industry=industry)


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/leadership")
def leadership():
    return render_template("leadership.html")


@app.get("/locations")
def locations():
    return render_template("locations.html")


@app.get("/careers")
def careers():
    return render_template("careers.html")


@app.get("/apply")
def apply_page():
    return render_template("apply.html")


@app.get("/contact-us")
def contact_page():
    return render_template("contact.html")


@app.get("/help-faq")
def help_faq():
    return render_template("help_faq.html")


def _field(name: str) -> str:
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        return (payload.get(name) or "").strip()
    return (request.form.get(name) or "").strip()


@app.post("/api/contact")
def contact():
    # Honeypot (bots tend to fill hidden fields)
    hp = _field("website")
    if hp:
        return jsonify({"ok": True})

    name = _field("name")
    email = _field("email")
    company = _field("company")
    phone = _field("phone")
    service = _field("service")
    message = _field("message")

    if not name or not email or not message:
        return jsonify({"ok": False, "error": "Name, email, and message are required."}), 400

    mail_to = MAIL_TO
    suppress_send = MAIL_SUPPRESS_SEND

    submitted_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subject = f"Website inquiry: {service or 'General'} — {name}"
    body = "\n".join(
        [
            "New website inquiry",
            "-------------------",
            f"Submitted: {submitted_at}",
            f"Name: {name}",
            f"Email: {email}",
            f"Company: {company or '-'}",
            f"Phone: {phone or '-'}",
            f"Service: {service or '-'}",
            "",
            "Message:",
            message,
        ]
    )

    # Auto-reply to the user from the admin mailbox (include their submitted details)
    user_subject = "We received your inquiry - Enmett"
    user_body = f"""Dear {name},

Thank you for contacting Enmett.

We have received your inquiry with the following details:

  Name: {name}
  Email: {email}
  Company: {company or '-'}
  Phone: {phone or '-'}
  Service: {service or '-'}

Your message:
{message}

Our team will review your request and get back to you shortly.

If anything looks incorrect or you want to add more information, you can simply reply to this email.

Best regards,
Enmett Team
"""

    if not suppress_send:
        # Use static mail settings defined at the top of this file.
        mail_server = MAIL_SERVER
        mail_port = MAIL_PORT
        mail_use_tls = MAIL_USE_TLS
        mail_use_ssl = MAIL_USE_SSL

        mail_username = MAIL_USERNAME
        mail_password = MAIL_PASSWORD
        mail_default_sender = MAIL_DEFAULT_SENDER or mail_username or "contact@enmett.com"

        admin_recipient = mail_to or mail_default_sender or mail_username

        # Message to admin / internal recipient
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = mail_default_sender
        msg["To"] = admin_recipient
        msg["Reply-To"] = email
        msg.set_content(body)

        # Auto-reply message to the user
        user_msg = EmailMessage()
        user_msg["Subject"] = user_subject
        user_msg["From"] = mail_default_sender
        user_msg["To"] = email
        user_msg.set_content(user_body)

        try:
            if mail_use_ssl:
                with smtplib.SMTP_SSL(mail_server, mail_port, timeout=20) as smtp:
                    smtp.login(mail_username, mail_password)
                    smtp.send_message(msg)
                    smtp.send_message(user_msg)
            else:
                with smtplib.SMTP(mail_server, mail_port, timeout=20) as smtp:
                    smtp.ehlo()
                    if mail_use_tls:
                        smtp.starttls()
                        smtp.ehlo()
                    smtp.login(mail_username, mail_password)
                    smtp.send_message(msg)
                    smtp.send_message(user_msg)
        except smtplib.SMTPAuthenticationError:
            return (
                jsonify(
                    {
                        "ok": False,
                        "error": "Email sending failed due to invalid SMTP username or password. Please contact the site administrator.",
                    }
                ),
                500,
            )
        except smtplib.SMTPException:
            return (
                jsonify(
                    {
                        "ok": False,
                        "error": "Email sending failed due to an SMTP error. Please try again later.",
                    }
                ),
                500,
            )
    return jsonify({"ok": True})


@app.post("/api/apply")
def apply():
    # Honeypot
    hp = _field("website")
    if hp:
        return jsonify({"ok": True})

    name = _field("name")
    email = _field("email")
    phone = _field("phone")
    role = _field("role")
    experience = _field("experience")
    location = _field("location")
    message = _field("message")
    resume = request.files.get("resume")

    if not name or not email or not resume:
        return (
            jsonify(
                {
                    "ok": False,
                    "error": "Name, email, and a PDF resume are required.",
                }
            ),
            400,
        )

    filename = (resume.filename or "").strip()
    if not filename.lower().endswith(".pdf"):
        return (
            jsonify(
                {
                    "ok": False,
                    "error": "Please upload your resume in PDF format.",
                }
            ),
            400,
        )

    mail_to = MAIL_TO
    suppress_send = MAIL_SUPPRESS_SEND

    submitted_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subject = f"Career application — {role or 'General'} — {name}"
    body = "\n".join(
        [
            "New career application",
            "----------------------",
            f"Submitted: {submitted_at}",
            f"Name: {name}",
            f"Email: {email}",
            f"Phone: {phone or '-'}",
            f"Role of interest: {role or '-'}",
            f"Experience: {experience or '-'}",
            f"Location: {location or '-'}",
            "",
            "Message:",
            message or "-",
        ]
    )

    user_subject = "We received your application - Enmett Careers"
    user_body = f"""Dear {name},

Thank you for applying to join Enmett.

We have received your application with the following details:

  Name: {name}
  Email: {email}
  Role of interest: {role or '-'}
  Experience: {experience or '-'}

Our team will review your application and contact you if your profile matches our current openings.

Best regards,
Enmett Careers Team
"""

    if not suppress_send:
        mail_server = MAIL_SERVER
        mail_port = MAIL_PORT
        mail_use_tls = MAIL_USE_TLS
        mail_use_ssl = MAIL_USE_SSL

        mail_username = MAIL_USERNAME
        mail_password = MAIL_PASSWORD
        mail_default_sender = MAIL_DEFAULT_SENDER or mail_username or "contact@enmett.com"

        admin_recipient = mail_to or mail_default_sender or mail_username

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = mail_default_sender
        msg["To"] = admin_recipient
        msg["Reply-To"] = email
        msg.set_content(body)

        try:
            resume_bytes = resume.read()
            if resume_bytes:
                msg.add_attachment(
                    resume_bytes,
                    maintype="application",
                    subtype="pdf",
                    filename=filename,
                )
        except Exception:
            # If attachment fails, still try to send the email without it.
            pass

        user_msg = EmailMessage()
        user_msg["Subject"] = user_subject
        user_msg["From"] = mail_default_sender
        user_msg["To"] = email
        user_msg.set_content(user_body)

        try:
            if mail_use_ssl:
                with smtplib.SMTP_SSL(mail_server, mail_port, timeout=20) as smtp:
                    smtp.login(mail_username, mail_password)
                    smtp.send_message(msg)
                    smtp.send_message(user_msg)
            else:
                with smtplib.SMTP(mail_server, mail_port, timeout=20) as smtp:
                    smtp.ehlo()
                    if mail_use_tls:
                        smtp.starttls()
                        smtp.ehlo()
                    smtp.login(mail_username, mail_password)
                    smtp.send_message(msg)
                    smtp.send_message(user_msg)
        except smtplib.SMTPAuthenticationError:
            return (
                jsonify(
                    {
                        "ok": False,
                        "error": "Email sending failed due to invalid SMTP username or password. Please contact the site administrator.",
                    }
                ),
                500,
            )
        except smtplib.SMTPException:
            return (
                jsonify(
                    {
                        "ok": False,
                        "error": "Email sending failed due to an SMTP error. Please try again later.",
                    }
                ),
                500,
            )

    return jsonify({"ok": True})


@app.get("/health")
def health():
    return jsonify({"ok": True})


if __name__ == "__main__":
    # 0.0.0.0 = listen on all interfaces so you can open via your IP (e.g. http://192.168.x.x:5000)
    app.run(host=FLASK_HOST, port=PORT, debug=FLASK_DEBUG)
