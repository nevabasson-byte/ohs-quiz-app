# questions.py - Expanded Advanced Database (20 Questions)

QUIZ_DATA = [
    {
        "question": "Under Section 37(2), an employer is liable for the conduct of a mandatary unless which condition is met?",
        "options": [
            "The employer provides all tools and equipment.",
            "A written agreement is signed acknowledging the mandatary's duty to comply with the Act.",
            "The mandatary has their own Letter of Good Standing.",
            "The inspector grants a verbal exemption."
        ],
        "answer": "A written agreement is signed acknowledging the mandatary's duty to comply with the Act.",
        "reference": "Section 37(2): Provisions regarding mandataries."
    },
    {
        "question": "Which section of the OHS Act stipulates that the CEO is the person ultimately accountable for safety compliance?",
        "options": ["Section 8", "Section 16(1)", "Section 17", "Section 38"],
        "answer": "Section 16(1)",
        "reference": "Section 16: Duty of chief executive officer."
    },
    {
        "question": "What is the legal definition of 'Reasonably Practicable' in Section 1?",
        "options": [
            "Cost is never a factor in safety decisions.",
            "Absolute safety must be guaranteed regardless of financial burden.",
            "A balance between the severity of the hazard and the cost/utility of mitigation.",
            "Compliance with international standards only."
        ],
        "answer": "A balance between the severity of the hazard and the cost/utility of mitigation.",
        "reference": "Section 1: Definitions."
    },
    {
        "question": "In terms of Section 17, at what employee count must an employer designate Health and Safety Representatives?",
        "options": [
            "Every workplace with 5+ employees.",
            "Workplaces with more than 20 employees.",
            "Only in high-risk factories.",
            "Only if requested by a trade union."
        ],
        "answer": "Workplaces with more than 20 employees.",
        "reference": "Section 17(1): Health and safety representatives."
    },
    {
        "question": "How many days does an employer have to perform a formal investigation into a reportable incident under GAR 9?",
        "options": ["24 hours", "7 days", "14 days", "30 days"],
        "answer": "7 days",
        "reference": "General Administrative Regulation 9(2)."
    },
    {
        "question": "According to Section 24, which of the following must be reported to an inspector immediately?",
        "options": [
            "An employee slipping without injury.",
            "A person becoming unconscious due to heat exhaustion.",
            "A minor cut requiring a basic bandage.",
            "Any employee taking a day of sick leave."
        ],
        "answer": "A person becoming unconscious due to heat exhaustion.",
        "reference": "Section 24(1)(b): Reportable incidents."
    },
    {
        "question": "Can a Section 16(2) appointee be held personally liable for a breach of the Act?",
        "options": [
            "No, only the CEO is liable.",
            "Yes, if they failed to perform the duties assigned to them in their letter of appointment.",
            "Only if they are the owner of the company.",
            "No, the company pays all fines so individuals are never liable."
        ],
        "answer": "Yes, if they failed to perform the duties assigned to them in their letter of appointment.",
        "reference": "Section 16(2) & Section 38: Offences and Penalties."
    },
    {
        "question": "Under General Safety Regulation 2, who is responsible for providing and maintaining PPE at no cost to the employee?",
        "options": ["The Employee", "The Trade Union", "The Employer", "The Department of Labour"],
        "answer": "The Employer",
        "reference": "General Safety Regulation 2(1)."
    },
    {
        "question": "What power does an inspector have under Section 30 of the Act?",
        "options": [
            "The power to fire an employee.",
            "The power to issue a prohibition notice to stop work immediately.",
            "The power to increase the CEO's salary.",
            "The power to change the company's registration name."
        ],
        "answer": "The power to issue a prohibition notice to stop work immediately.",
        "reference": "Section 30: Special powers of inspectors."
    },
    {
        "question": "When must a Health and Safety Committee meet at a minimum?",
        "options": [
            "Once a week.",
            "At least once every three months.",
            "Only after a serious accident.",
            "Once a year."
        ],
        "answer": "At least once every three months.",
        "reference": "Section 19(4): Health and safety committees."
    },
    {
        "question": "Under Section 9, what is the employer's duty to persons other than their employees (e.g., the public or visitors)?",
        "options": [
            "No duty exists; visitors enter at their own risk.",
            "To ensure they are not exposed to hazards to their health and safety.",
            "To provide them with a full medical exam before entry.",
            "Only to sign an indemnity form."
        ],
        "answer": "To ensure they are not exposed to hazards to their health and safety.",
        "reference": "Section 9: General duties of employers to persons other than employees."
    },
    {
        "question": "Which of the following must be included in an Annexure 1 incident record?",
        "options": [
            "The employee's home address.",
            "A detailed description of the incident and the root cause.",
            "The employee's political affiliation.",
            "The company's profit margin for that month."
        ],
        "answer": "A detailed description of the incident and the root cause.",
        "reference": "General Administrative Regulation 9(1)."
    },
    {
        "question": "In a workplace with 100 employees, what is the minimum number of H&S Representatives required for a factory environment?",
        "options": ["1", "2", "4", "10"],
        "answer": "2",
        "reference": "Section 17(2): 1 per 50 employees in shops/offices, 1 per 20 elsewhere (Standard interpreted)."
    },
    {
        "question": "Can an employee refuse to use PPE provided by the employer?",
        "options": [
            "Yes, if they find it uncomfortable.",
            "No, Section 14(c) requires employees to carry out any lawful order regarding health and safety.",
            "Yes, if they buy their own.",
            "Only if the H&S Representative agrees."
        ],
        "answer": "No, Section 14(c) requires employees to carry out any lawful order regarding health and safety.",
        "reference": "Section 14: General duties of employees."
    },
    {
        "question": "What is the maximum fine for a standard contravention of the Act (excluding Section 38 negligence)?",
        "options": ["R5,000", "R50,000", "R100,000", "R1,000,000"],
        "answer": "R50,000",
        "reference": "Section 38: Offences, penalties and special orders."
    },
    {
        "question": "Who must chair the Health and Safety Committee meeting?",
        "options": [
            "The CEO.",
            "An Inspector.",
            "The committee members elect a chairperson.",
            "The most senior employee."
        ],
        "answer": "The committee members elect a chairperson.",
        "reference": "Section 19(5): Health and safety committees."
    },
    {
        "question": "Under Section 37(1), can an employer be held liable for an employee's mistake if they were acting outside their scope of authority?",
        "options": [
            "Never.",
            "Yes, unless the employer proves they forbade the act and took reasonable steps to prevent it.",
            "Always, without exception.",
            "Only if the employee is a manager."
        ],
        "answer": "Yes, unless the employer proves they forbade the act and took reasonable steps to prevent it.",
        "reference": "Section 37(1): Acts or omissions by employees."
    },
    {
        "question": "Which regulation governs the safety of stacked materials in a warehouse?",
        "options": [
            "General Safety Regulation 8",
            "Construction Regulation 10",
            "General Administrative Regulation 4",
            "Facilities Regulation 2"
        ],
        "answer": "General Safety Regulation 8",
        "reference": "GSR 8: Stacking of articles."
    },
    {
        "question": "What is the primary function of a Health and Safety Representative?",
        "options": [
            "To arrest employees who break rules.",
            "To review the effectiveness of health and safety measures and perform inspections.",
            "To do the cleaning in the workshop.",
            "To manage the company's payroll."
        ],
        "answer": "To review the effectiveness of health and safety measures and perform inspections.",
        "reference": "Section 18: Functions of health and safety representatives."
    },
    {
        "question": "If an inspector issues a 'Correction Notice' under Section 30, can the employer appeal it?",
        "options": [
            "No, the inspector's word is final.",
            "Yes, by appealing to the Chief Inspector within 60 days.",
            "Yes, by appealing to the Chief Inspector within 30 days.",
            "Only if they pay a fine first."
        ],
        "answer": "Yes, by appealing to the Chief Inspector within 60 days.",
        "reference": "Section 35: Appeal against decision of inspector."
    }
]