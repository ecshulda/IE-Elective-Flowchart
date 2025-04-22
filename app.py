
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Industrial Engineering Elective Flowchart</h1>", unsafe_allow_html=True)

# Background image
st.image("ie_flowchart_home.png", use_container_width=True)

# CSS overlays with JS-compatible links instead of HTML form submissions
st.markdown("""
<style>
.container {
    position: relative;
    width: 1200px;
    height: 950px;
    margin: auto;
    margin-top: -950px;
    z-index: 2;
}
.overlay-button {
    position: absolute;
    background-color: rgba(0, 255, 0, 0.4);
    border: none;
    width: 100%;
    height: 100%;
    cursor: pointer;
    text-decoration: none;
    display: block;
}
#dataAnalytics { left: 470px; top: 370px; width: 111px; height: 71px; }
#imseElective1 { left: 910px; top: 460px; width: 111px; height: 71px; }
#imseElective2 { left: 1030px; top: 250px; width: 111px; height: 71px; }
#engineeringElective1 { left: 620px; top: 655px; width: 121px; height: 81px; }
#engineeringElective2 { left: 750px; top: 655px; width: 111px; height: 81px; }
</style>

<div class="container">
    <a href="/?clicked=Data%20Analytics" class="overlay-button" id="dataAnalytics"></a>
    <a href="/?clicked=IMSE%20Elective%201" class="overlay-button" id="imseElective1"></a>
    <a href="/?clicked=IMSE%20Elective%202" class="overlay-button" id="imseElective2"></a>
    <a href="/?clicked=Engineering%20Elective%201" class="overlay-button" id="engineeringElective1"></a>
    <a href="/?clicked=Engineering%20Elective%202" class="overlay-button" id="engineeringElective2"></a>
</div>
""", unsafe_allow_html=True)

# Use updated query param API
clicked = st.query_params.get("clicked", None)
if clicked:
    st.session_state.clicked = clicked

if "clicked" in st.session_state:
    which = st.session_state.clicked

    if which == "Data Analytics":
        st.markdown("""
        <h3>Data Analytics Elective Options</h3>
        <ol>
            <li><b>IMSE 441 – Experimental Design</b><br>
            <b>Offered in:</b> Fall and Spring<br>
            <b>Overview:</b> Design experiments and analyze results.<br>
            <b>Technical Skills:</b> ANOVA, factorial design, statistical testing<br>
            <b>Durable Skills:</b> Data analysis, precision, critical thinking<br>
            <b>⚠️ Note:</b> This course can only be selected once—either as a Data Analytics or IMSE elective.</li><br>
            <li><b>STAT 705 – Regression and ANOVA</b><br>
            <b>Offered in:</b> Fall<br>
            <b>Overview:</b> Regression modeling and ANOVA techniques.<br>
            <b>Technical Skills:</b> Linear models, diagnostics<br>
            <b>Durable Skills:</b> Statistical reasoning, modeling</li><br>
            <li><b>STAT 511 – Statistical Methods I</b><br>
            <b>Offered in:</b> Fall and Spring<br>
            <b>Overview:</b> Core stats for data analysis.<br>
            <b>Technical Skills:</b> Descriptive stats, hypothesis testing<br>
            <b>Durable Skills:</b> Quantitative reasoning, critical thinking</li>
        </ol>
        """, unsafe_allow_html=True)
    elif which == "IMSE Elective 1":
        st.markdown(f"""<ol>
    <li><b>IMSE 441 – Introduction to Analytics</b><br>
    <b>Offered in:</b> Fall and Spring<br>
    <b>Overview:</b> Learn how to analyze data and make decisions using Pythonwithout needing to be a programming wizard. Youll work with real-world datasets to perform statistical analysis, test hypotheses, build regression models, and create visualizations that inform better decisions in industrial engineering.<br>
    <b>Technical Skills:</b> Python (Pandas, NumPy, Matplotlib), Data wrangling, Descriptive statistics, Hypothesis testing, Confidence intervals, Linear regression, Multivariate analysis, Data visualization<br>
    <b>Durable Skills:</b> Analytical thinking, Programming literacy, Data-driven decision making, Technical writing (reports), Teamwork (group projects), Communicating complex ideas clearly<br><b>⚠️ Note:</b> This course can only be selected once—either as a Data Analytics or IMSE elective.<br></li><br>
    
    <li><b>IMSE 564 – Product and Process Engineering</b><br>
    <b>Offered in:</b> Fall<br>
    <b>Overview:</b> Learn how product design and manufacturing process choices affect cost, quality, and efficiency. You'll explore design for manufacturability, tool design, assembly methods, and how engineers create systems that bring great products to life.<br>
    <b>Technical Skills:</b> Design for manufacturability (DFM), Tool engineering basics, Tolerance analysis, Geometric dimensioning & tolerancing (GD&T), Process selection for additive/subtractive manufacturing<br>
    <b>Durable Skills:</b> Engineering judgment, System-level thinking, Communication of technical concepts, Cost-conscious design thinking, Collaborative problem-solving<br></li><br>
    
    <li><b>IMSE 602 – Topics in Industrial Engineering / Skill X</b><br>
    <b>Offered in:</b> All Terms<br>
    <b>Overview:</b> A career accelerator that teaches you to build your career like a startup. Youll define your direction, build a differentiated skill set, apply your skills through high-impact experiences, and grow a powerful network. Designed to help you graduate with more than just a resumeyoull graduate with a competitive edge.<br>
    <b>Technical Skills:</b> Resume & portfolio development, LinkedIn optimization, Skill-Rich Opportunity (SRO) mapping, Networking outreach, Career storytelling<br>
    <b>Durable Skills:</b> Career strategy, Self-awareness, Personal branding, Communication, Relationship building, Growth mindset<br></li><br>
    
    <li><b>IMSE 605 – Advanced Industrial Management</b><br>
    <b>Offered in:</b> Fall<br>
    <b>Overview:</b> Learn how modern management philosophies impact engineers and teams. Youll explore leadership, planning, ethics, globalization, team building, and decision-making tools to become a more effective technical leader. Great for engineers eyeing management or project leadership roles.<br>
    <b>Technical Skills:</b> Strategic planning, SWOT & AHP/TOPSIS analysis, Evidence-based decision-making, Organizational design, Total quality management<br>
    <b>Durable Skills:</b> Leadership development, Ethical reasoning, Cross-cultural awareness, Team collaboration, Communication and conflict resolution<br></li><br>
    
    <li><b>IMSE 625 – Work Environments</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how to design safer, more efficient, and human-friendly workplaces by studying how people physically interact with tools, environments, and systems. Topics include ergonomics, toxicology, noise, lighting, temperature, and how these impact worker health, safety, and performance.<br>
    <b>Technical Skills:</b> Ergonomic assessment, Anthropometric data application, Manual material handling analysis, Environmental hazard evaluation (noise, lighting, heat), Workstation and display design<br>
    <b>Durable Skills:</b> Human-centered design thinking, Workplace safety analysis, Technical presentation (oral & written), Critical thinking, Cross-disciplinary application of engineering and life sciences<br></li><br>
    
    <li><b>IMSE 710 – Transportation Logistics</b><br>
    <b>Offered in:</b> Fall (Even Years)<br>
    <b>Overview:</b> Learn how to design and analyze supply chain systems, with a focus on freight transportation and logistics. Youll use quantitative models to solve real-world problems in routing, facility location, and resource schedulingand learn how to communicate your solutions effectively.	<br>
    <b>Technical Skills:</b> Freight mode selection & routing, Facility location modeling, Logistics resource scheduling, Supply chain coordination modeling, Quantitative decision analysis<br>
    <b>Durable Skills:</b> Decision-making under complexity, Analytical modeling, Technical communication, Systems thinking, Applied problem-solving<br></li><br>
    
    <li><b>IMSE 785 – Big Data Analytics</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how to manage, analyze, and visualize massive datasets using tools like Hadoop, Spark, and machine learning. This course covers everything from data storage and retrieval to real-time analytics and AI model training. Ideal for future data engineers and analysts.<br>
    <b>Technical Skills:</b> Hadoop & Spark, SQL/NoSQL querying, Machine learning with PySpark, Data wrangling & ingestion, Data visualization & dashboarding<br>
    <b>Durable Skills:</b> Problem-solving with data, Communication of insights, Strategic tech planning, Collaboration on complex data projects, Adaptability to new tools<br></li><br>
    </ol>""", unsafe_allow_html=True)
    elif which == "IMSE Elective 2":
        st.markdown(f"""<ol>
    <li><b>IMSE 441 – Introduction to Analytics</b><br>
    <b>Offered in:</b> Fall and Spring<br>
    <b>Overview:</b> Learn how to analyze data and make decisions using Pythonwithout needing to be a programming wizard. Youll work with real-world datasets to perform statistical analysis, test hypotheses, build regression models, and create visualizations that inform better decisions in industrial engineering.<br>
    <b>Technical Skills:</b> Python (Pandas, NumPy, Matplotlib), Data wrangling, Descriptive statistics, Hypothesis testing, Confidence intervals, Linear regression, Multivariate analysis, Data visualization<br>
    <b>Durable Skills:</b> Analytical thinking, Programming literacy, Data-driven decision making, Technical writing (reports), Teamwork (group projects), Communicating complex ideas clearly<br><b>⚠️ Note:</b> This course can only be selected once—either as a Data Analytics or IMSE elective.<br></li><br>
    
    <li><b>IMSE 562 – Materials and the Impact of Manufacturing Processes</b><br>
    <b>Offered in:</b> Spring<br>
    <b>Overview:</b> Understand how different materials behave and how manufacturing processeslike 3D printing or microfabricationchange their properties. Includes hands-on labs where students test, measure, and analyze materials in real-world conditions.<br>
    <b>Technical Skills:</b> Materials characterization, Experimental design, Microscopy, Additive manufacturing, Semiconductor processes, Process modeling<br>
    <b>Durable Skills:</b> Critical thinking, Technical communication, Independent problem-solving, Team collaboration, Systems thinking<br></li><br>
    
    <li><b>IMSE 602 – Topics in Industrial Engineering / Skill X</b><br>
    <b>Offered in:</b> All Terms<br>
    <b>Overview:</b> A career accelerator that teaches you to build your career like a startup. Youll define your direction, build a differentiated skill set, apply your skills through high-impact experiences, and grow a powerful network. Designed to help you graduate with more than just a resumeyoull graduate with a competitive edge.<br>
    <b>Technical Skills:</b> Resume & portfolio development, LinkedIn optimization, Skill-Rich Opportunity (SRO) mapping, Networking outreach, Career storytelling<br>
    <b>Durable Skills:</b> Career strategy, Self-awareness, Personal branding, Communication, Relationship building, Growth mindset<br></li><br>
    
    <li><b>IMSE 625 – Work Environments</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how to design safer, more efficient, and human-friendly workplaces by studying how people physically interact with tools, environments, and systems. Topics include ergonomics, toxicology, noise, lighting, temperature, and how these impact worker health, safety, and performance.<br>
    <b>Technical Skills:</b> Ergonomic assessment, Anthropometric data application, Manual material handling analysis, Environmental hazard evaluation (noise, lighting, heat), Workstation and display design<br>
    <b>Durable Skills:</b> Human-centered design thinking, Workplace safety analysis, Technical presentation (oral & written), Critical thinking, Cross-disciplinary application of engineering and life sciences<br></li><br>
    
    <li><b>IMSE 641 – Quality Engineering</b><br>
    <b>Offered in:</b> Spring<br>
    <b>Overview:</b> Learn how to use data, AI, and advanced tools to monitor and improve quality in manufacturing and healthcare. Youll apply statistical process control, automate inspections, and explore modern quality systems like Six Sigma and ISO 9000.<br>
    <b>Technical Skills:</b> Statistical Process Control (SPC), Machine learning for quality data, Python programming for analysis, Visual inspection systems, Multivariate quality monitoring<br>
    <b>Durable Skills:</b> Analytical thinking, Data interpretation, Continuous improvement mindset, Quality-focused problem-solving, Adaptability to emerging tech<br></li><br>
    
    <li><b>IMSE 664 – Additive Manufacturing</b><br>
    <b>Offered in:</b> Spring<br>
    <b>Overview:</b> Dive into the world of 3D printing for healthcarelearn how to create medical models, prosthetics, and more using state-of-the-art tools and real patient data. You'll blend hands-on lab work with project-based learning, building both your technical and communication skills for real-world healthcare collaboration.<br>
    <b>Technical Skills:</b> 3D printing with polymers/metals/biomaterials, CAD modeling & STL file prep, Medical imaging-to-print workflow, Extrusion & vat-polymerization techniques, G-code & print control<br>
    <b>Durable Skills:</b> Cross-disciplinary communication, Project-based collaboration, Innovation in healthcare contexts, Technical writing & presentation, Adaptability in emerging tech environments<br></li><br>
    
    <li><b>IMSE 751 – Normative Theory of Decisions and Games</b><br>
    <b>Offered in:</b> Spring<br>
    <b>Overview:</b> Learn how to make smart decisions under uncertainty and how strategic players behave in competitive environments. Youll study decision analysis and game theory to solve problems involving risk, competition, and collaboration.<br>
    <b>Technical Skills:</b> Decision trees, Bayesian inference, Utility theory, Nash equilibrium modeling, Multi-criteria decision analysis<br>
    <b>Durable Skills:</b> Strategic thinking, Structured reasoning, Ethical decision-making, Analytical communication, Modeling uncertainty<br></li><br>
    
    <li><b>IMSE 752 – Multiple Criteria Decision Analysis</b><br>
    <b>Offered in:</b> Spring (Even Years)<br>
    <b>Overview:</b> Learn how to make structured decisions when faced with multiple conflicting objectives. Youll explore real-world applications using techniques like value modeling, goal programming, and outranking methods for both individuals and groups.<br>
    <b>Technical Skills:</b> Value function modeling, Goal and aspiration-based analysis, Outranking methods (e.g. ELECTRE), Preference structuring, Multi-criteria evaluation frameworks<br>
    <b>Durable Skills:</b> Critical thinking, Structured decision-making, Clarity in presenting trade-offs, Synthesis of conflicting priorities, Analytical reasoning<br></li><br>
    
    <li><b>IMSE 785 – Big Data Analytics</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how to manage, analyze, and visualize massive datasets using tools like Hadoop, Spark, and machine learning. This course covers everything from data storage and retrieval to real-time analytics and AI model training. Ideal for future data engineers and analysts.<br>
    <b>Technical Skills:</b> Hadoop & Spark, SQL/NoSQL querying, Machine learning with PySpark, Data wrangling & ingestion, Data visualization & dashboarding<br>
    <b>Durable Skills:</b> Problem-solving with data, Communication of insights, Strategic tech planning, Collaboration on complex data projects, Adaptability to new tools<br></li><br>
    </ol>""", unsafe_allow_html=True)
    elif which == "Engineering Elective 1":
        st.markdown(f"""<ol>
    <li><b>BAE 345 – Properties of Biological Materials</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Explore the physical, chemical, thermal, and mechanical properties of biological materialslike plants, food, and bio-based materialsand how they behave in real-world systems. Youll learn how to measure things like moisture content, density, porosity, and fluid behavior, and apply those insights to designing better agricultural and biological processes.<br>
    <b>Technical Skills:</b> Moisture content analysis, Rheological modeling, Density & surface area calculations, Stress-strain analysis, Equilibrium moisture content modeling, Power-law fluid analysis<br>
    <b>Durable Skills:</b> Critical thinking, Quantitative problem solving, Scientific communication, Application of engineering principles to real-world biological systems, Precision and data accuracy</li><br>
    
    <li><b>BAE 346 – Properties of Biological Materials Laboratory</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Hands-on lab course where students test and analyze the physical, chemical, and rheological properties of biological materials like soils, proteins, and bioproducts. Youll learn to use lab tools like pipettes, gel electrophoresis, and rheometers, while applying Excel and data analysis to interpret scientific results.<br>
    <b>Technical Skills:</b> Moisture content & density testing, Gel electrophoresis, Rheological measurement, Soil sampling & texture classification, Excel data analysis, Protein quantification, Power-law fluid modeling<br>
    <b>Durable Skills:</b> Scientific data communication, Lab report writing, Critical thinking, Team-based problem solving, Precision in experimentation</li><br>
    
    <li><b>CE 333 – Statics</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how forces act on objects that dont move. This course covers how to break down, analyze, and solve real-world equilibrium problems involving structures, machines, cables, and more. You'll work with vectors, free-body diagrams, moments, friction, and center of gravityall essential tools for future civil, mechanical, and structural engineers.<br>
    <b>Technical Skills:</b> Vector algebra, Free-body diagramming, Force/moment calculation, Friction modeling, Truss & frame analysis, Center of gravity & moment of inertia calculations<br>
    <b>Durable Skills:</b> Analytical reasoning, Engineering problem-solving, Visual-spatial skills, Self-learning from practice problems, Attention to precision and method</li><br>
    
    <li><b>CE 533 – Mechanics of Materials</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how materials respond to forces and moments in real-world structures. This course covers stress, strain, deformation, and failure in beams, shafts, and pressure vessels. Youll calculate internal forces, deflections, and design members under axial, bending, shear, and torsional loads.<br>
    <b>Technical Skills:</b> Stress-strain analysis, Beam deflection calculations, Mohrs circle, Combined loading, Principal stresses, Material failure criteria<br>
    <b>Durable Skills:</b> Engineering judgment, Technical problem-solving, Attention to detail, Structural visualization, Applied mechanics thinking</li><br>
    
    <li><b>CHE 521 – Chemical Engineering Thermodynamics 2</b><br>
    <b>Offered in:</b> Fall<br>
    <b>Overview:</b> Deepen your understanding of thermodynamics by analyzing phase behavior and chemical reactions. This course covers advanced topics like fugacity, activity models, phase equilibrium, and reaction equilibriumcritical tools for designing chemical processes and systems.<br>
    <b>Technical Skills:</b> Fugacity & chemical potential calculations, Phase diagram interpretation, Vapor-liquid equilibrium (VLE), Reaction equilibrium modeling, Activity coefficient models, Thermodynamic software use<br>
    <b>Durable Skills:</b> Complex system modeling, Analytical problem-solving, Quantitative reasoning, Scientific precision, Interpreting multivariable interactions</li><br>
    </ol>""", unsafe_allow_html=True)
    elif which == "Engineering Elective 2":
        st.markdown(f"""<ol>
    <li><b>BAE 345 – Properties of Biological Materials</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Explore the physical, chemical, thermal, and mechanical properties of biological materialslike plants, food, and bio-based materialsand how they behave in real-world systems. Youll learn how to measure things like moisture content, density, porosity, and fluid behavior, and apply those insights to designing better agricultural and biological processes.<br>
    <b>Technical Skills:</b> Moisture content analysis, Rheological modeling, Density & surface area calculations, Stress-strain analysis, Equilibrium moisture content modeling, Power-law fluid analysis<br>
    <b>Durable Skills:</b> Critical thinking, Quantitative problem solving, Scientific communication, Application of engineering principles to real-world biological systems, Precision and data accuracy</li><br>
    
    <li><b>BAE 346 – Properties of Biological Materials Laboratory</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Hands-on lab course where students test and analyze the physical, chemical, and rheological properties of biological materials like soils, proteins, and bioproducts. Youll learn to use lab tools like pipettes, gel electrophoresis, and rheometers, while applying Excel and data analysis to interpret scientific results.<br>
    <b>Technical Skills:</b> Moisture content & density testing, Gel electrophoresis, Rheological measurement, Soil sampling & texture classification, Excel data analysis, Protein quantification, Power-law fluid modeling<br>
    <b>Durable Skills:</b> Scientific data communication, Lab report writing, Critical thinking, Team-based problem solving, Precision in experimentation</li><br>
    
    <li><b>CE 333 – Statics</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how forces act on objects that dont move. This course covers how to break down, analyze, and solve real-world equilibrium problems involving structures, machines, cables, and more. You'll work with vectors, free-body diagrams, moments, friction, and center of gravityall essential tools for future civil, mechanical, and structural engineers.<br>
    <b>Technical Skills:</b> Vector algebra, Free-body diagramming, Force/moment calculation, Friction modeling, Truss & frame analysis, Center of gravity & moment of inertia calculations<br>
    <b>Durable Skills:</b> Analytical reasoning, Engineering problem-solving, Visual-spatial skills, Self-learning from practice problems, Attention to precision and method</li><br>
    
    <li><b>CE 530 – Statics and Dynamics</b><br>
    <b>Offered in:</b> Spring<br>
    <b>Overview:</b> Learn how to analyze objects at rest and in motionfrom bridges to machines. Youll calculate forces, torques, acceleration, and energy to understand how systems stay still or move. Great for students interested in mechanical or structural design.<br>
    <b>Technical Skills:</b> Free-body diagramming, Truss and frame analysis, Moment of inertia calculations, Work-energy analysis, Newtons law applications<br>
    <b>Durable Skills:</b> Analytical reasoning, Structured problem-solving, Engineering logic, Precision in calculation, Persistence through complexity</li><br>
    
    <li><b>CE 533 – Mechanics of Materials</b><br>
    <b>Offered in:</b> Unknown<br>
    <b>Overview:</b> Learn how materials respond to forces and moments in real-world structures. This course covers stress, strain, deformation, and failure in beams, shafts, and pressure vessels. Youll calculate internal forces, deflections, and design members under axial, bending, shear, and torsional loads.<br>
    <b>Technical Skills:</b> Stress-strain analysis, Beam deflection calculations, Mohrs circle, Combined loading, Principal stresses, Material failure criteria<br>
    <b>Durable Skills:</b> Engineering judgment, Technical problem-solving, Attention to detail, Structural visualization, Applied mechanics thinking</li><br>
    </ol>""", unsafe_allow_html=True)
