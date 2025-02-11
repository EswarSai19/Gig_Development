//
function toggleEditForm() {
  const form = document.getElementById("edit-form");

  // Check for both 'none' and default (empty) state
  if (form.style.display === "none" || form.style.display === "") {
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }
}

function saveChanges() {
  const name = document.getElementById("edit-name").value;
  const title = document.getElementById("edit-title").value;
  const email = document.getElementById("edit-email").value;
  const phone = document.getElementById("edit-phone").value;
  const linkedin = document.getElementById("edit-linkedin").value;
  const company = document.getElementById("edit-company").value;

  const profileImageInput = document.getElementById("edit-image");
  const profileImage = document.getElementById("profile-image");

  if (profileImageInput.files && profileImageInput.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      profileImage.src = e.target.result;
    };
    reader.readAsDataURL(profileImageInput.files[0]);
  }

  document.getElementById("profile-name").textContent = name;
  document.getElementById("profile-title").textContent = title;
  document.getElementById("profile-email").textContent = email;
  document.getElementById("profile-phone").textContent = phone;
  document.getElementById("profile-linkedin").href = linkedin;
  document.getElementById("profile-linkedin").textContent = linkedin;
  document.getElementById("profile-company").textContent = company;

  toggleEditForm();
}

// Update Profile Image
function updateProfileImage(event) {
  const input = event.target;
  const reader = new FileReader();

  reader.onload = function () {
    const displayImg = document.getElementById("display-img");
    displayImg.src = reader.result;
  };

  if (input.files && input.files[0]) {
    reader.readAsDataURL(input.files[0]);
  }
}

function toggleProfileMenu() {
  const menu = document.getElementById("profile-menu");
  menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Update profile from localStorage (sync with profile.html)
function updateProfileHeader() {
  const initials = localStorage.getItem("profileInitials") || "Guest";
  const name = localStorage.getItem("profileName") || "Guest";
  const email = localStorage.getItem("profileEmail") || "guest@example.com";

  document.getElementById("profile-initials").textContent = initials;
  document.getElementById("profile-name-dropdown").textContent = name;
  document.getElementById("profile-email-dropdown").textContent = email;
}

// Call on page load
document.addEventListener("DOMContentLoaded", updateProfileHeader);

// New part of the file
const skillsInput = document.getElementById("skills-required");
const suggestionsList = document.getElementById("suggestions-list");
const selectedSkillsContainer = document.getElementById("selected-skills");
const hiddenSkillsInput = document.getElementById("skills-list"); // Hidden input
const availableSkills = [
  "Python",
  "Java",
  "JavaScript",
  "C#",
  "C++",
  "Ruby",
  "PHP",
  "Kotlin",
  "Swift",
  "HTML5",
  "CSS3",
  "React.js",
  "Angular",
  "Vue.js",
  "SASS",
  "Bootstrap",
  "Node.js",
  "Django",
  "Flask",
  "Spring Boot",
  ".NET",
  "Express.js",
  "SQL",
  "PostgreSQL",
  "MongoDB",
  "MySQL",
  "Oracle",
  "Redis",
  "Git",
  "GitHub",
  "GitLab",
  "Bitbucket",
  "Docker",
  "Kubernetes",
  "Jenkins",
  "Ansible",
  "Terraform",
  "AWS",
  "Azure",
  "Google Cloud Platform (GCP)",
  "RESTful APIs",
  "GraphQL",
  "SOAP",
  "Jest",
  "Mocha",
  "Jasmine",
  "Selenium",
  "Cypress",
  "Refactoring",
  "Profiling",
  "Debugging",
  "Visual Studio Code",
  "IntelliJ IDEA",
  "Eclipse",
  "PyCharm",
  "React Native",
  "Flutter",
  "Android Studio",
  "Xamarin",
  "JIRA",
  "Trello",
  "Asana",
  "Microsoft Project",
  "Scrum",
  "Kanban",
  "SAFe",
  "Lean",
  "CI/CD pipelines",
  "Release Automation",
  "Incident Management",
  "AWS CloudFormation",
  "Azure DevOps",
  "GCP Deployment Manager",
  "Python",
  "JavaScript",
  "SQL",
  "Data Modeling",
  "Microservices",
  "Monolithic Architecture",
  "Event-Driven Architecture",
  "ARM (Active Risk Manager)",
  "RiskWatch",
  "Postman",
  "Tableau",
  "Power BI",
  "Google Analytics",
  "JIRA",
  "Confluence",
  "Rally",
  "Lucidchart",
  "SQL",
  "Excel (Advanced)",
  "Power BI",
  "Tableau",
  "BPMN",
  "Visio",
  "Bizagi",
  "ARIS",
  "UML Modeling",
  "Use Case Diagrams",
  "Sequence Diagrams",
  "Class Diagrams",
  "Postman",
  "Selenium",
  "Figma",
  "Adobe XD",
  "Axure RP",
  "Balsamiq",
  "Salesforce",
  "SAP",
  "Microsoft Dynamics",
  "User Stories",
  "Sprint Planning",
  "Backlog Grooming",
  "APIs",
  "ETL Processes",
  "Middleware",
  "TestRail",
  "Zephyr",
  "HP ALM",
  "Selenium",
  "Cypress",
  "Playwright",
  "Appium",
  "Katalon Studio",
  "JMeter",
  "LoadRunner",
  "Gatling",
  "Postman",
  "SoapUI",
  "Swagger",
  "OWASP ZAP",
  "Burp Suite",
  "Nessus",
  "Git",
  "GitHub",
  "JIRA",
  "Bugzilla",
  "TestLink",
  "Jenkins",
  "CircleCI",
  "Bamboo",
  "Python",
  "Java",
  "JavaScript",
  "Appium",
  "Espresso",
  "XCTest",
  "SQL",
  "Oracle DB",
  "AWS Device Farm",
  "Sauce Labs",
  "BrowserStack",
  ".NET Developer",
  "Accessibility Specialist",
  "Admin Big Data",
  "Administrative Assistant",
  "Adobe Acrobat Expert",
  "Adobe After Effects Specialist",
  "Adobe Illustrator Expert",
  "Adobe InDesign Expert",
  "Adobe Photoshop Expert",
  "Adobe Premiere Pro Specialist",
  "Agile Project Manager",
  "Airtable Freelancer",
  "Alexa Skill Kit Specialist",
  "Amazon EC2 Specialist",
  "Android App Developer",
  "Android Developer",
  "Android Studio Freelancer",
  "Anime Freelancer",
  "Ansible Automation Engineer",
  "Ansible Operations Engineer",
  "ANSYS Specialist",
  "Apache Spark Specialist",
  "API Developer",
  "App Store Specialist",
  "AppDynamics Engineer",
  "Apple Xcode Specialist",
  "Application Security Engineer",
  "ArcGIS Developer",
  "Arduino Programmer",
  "Artifactory Engineer",
  "Artificial Intelligence (AI) / Machine Learning Engineer",
  "Artificial intelligence / Machine Learning Engineer",
  "Artificial intelligence Architect",
  "Artificial Intelligence Engineer",
  "Artificial Intelligence Researcher",
  "ASP.NET Developer",
  "AutoCAD Specialist",
  "AWS Developer",
  "AWS DevOps Engineer",
  "AWS Solutions Architect",
  "Azure DevOps Engineer",
  "Babylon.js Freelancer",
  "Bamboo Engineer",
  "Big Data Architect",
  "Big Data Engineer",
  "Big Data Specialist",
  "BigQuery Developer",
  "Bitbucket Engineer",
  "Blockchain Developer",
  "Bot Developer",
  "Build and Release Engineer",
  "Build Engineer",
  "Business Systems Analyst",
  "C# Developer",
  "C# Developers & Programmer",
  "C++ Programmers & Developer",
  "CAD Designer",
  "Chat Support Specialist",
  "Chatbot Developer",
  "Chief Architect Specialist",
  "Chief Operations Engineer",
  "Chrome Extension Developer",
  "Cloud administrator",
  "Cloud Architect",
  "Cloud automation engineer",
  "Cloud Computing Specialist",
  "Cloud engineer",
  "Cloud network engineer",
  "Cloud Security Engineer",
  "CNC Programmer",
  "CodeIgniter Developer",
  "Coder",
  "Cold Caller",
  "Computational Fluid Dynamics (CFD) Specialist",
  "Computer Hardware Engineer",
  "Computer Network Architect",
  "Computer Programmer",
  "Computer Research Scientist",
  "Computer Systems Analyst",
  "Computer Vision Engineer",
  "Confluence Engineer",
  "Consul Engineer",
  "CorelDRAW Specialist",
  "Coverage.py Engineer",
  "CRM Specialist",
  "CSS Developer",
  "d3.js Developer",
  "Data Analysts",
  "Data Architect",
  "Data Cleansing Analyst",
  "Data Engineer",
  "Data Entry Specialist",
  "Data Extraction Specialist",
  "Data Miner",
  "Data Modeler",
  "Data Scientist",
  "Data Scraper",
  "Data Visualization Specialist",
  "Database Administrator",
  "Database Designer",
  "Datadog Engineer",
  "Delphi Developer",
  "DevOps Architect",
  "DevOps Engineer",
  "Devops Manager",
  "DevSecOps Architect",
  "DevSecOps Engineer",
  "Django Freelancer",
  "Docker Engineer",
  "Docker Specialist",
  "Electrical Drawing Specialist",
  "Elementor Freelancer",
  "ELK Engineer",
  "Embedded Software Engineer",
  "Engineering Drawing Specialist",
  "Entry Level Developer",
  "Entry Level Network Engineer",
  "Entry Level Programmer",
  "Entry Level Software Developer",
  "Entry Level Software Engineer",
  "Entry Level Web Developer",
  "Erlang Developers & Programmer",
  "ERPNext Specialist",
  "ESP32 Freelancer",
  "Etsy Administration Specialist",
  "Falco Engineer",
  "FFmpeg Specialist",
  "Figma Freelancer",
  "FluentD Engineer",
  "Flutter Developer",
  "Fortify Engineer",
  "Front End Web Developer",
  "Front end Desiner",
  "Full Stack Developer",
  "Full Stack JAVA Developer/Programmer/Engineer",
  "Full Stack Python Developer/Programmer/Engineer",
  "Fusion 360 Specialist",
  "Game Developer",
  "GCP DevOps Engineer",
  "Gerrit Administrator",
  "Gerrit Engineer",
  "Git Engineer",
  "Github Engineer",
  "GitLab Engineer",
  "Gradle Engineer",
  "Grafana Engineer",
  "Groovy Engineer",
  "Information Architect",
  "Information Security Analyst",
  "IOS Developer",
  "Istio Engineer",
  "IT Manager",
  "JaCoCO Engineer",
  "Java Developer",
  "JavaScript Developer",
  "Jenkins Engineer",
  "Jira Administrator",
  "JIRA Engineer",
  "JUnit Engineer",
  "kubernetes Administrator",
  "Kubernetes Engineer",
  "Kubernetes Operations Engineer",
  "Machine learning Architect",
  "Machine Learning Engineer",
  "Micro services / API Lead Designer",
  "Mobile Application Developer",
  "Mulesoft Developer",
  "Nagios Engineer",
  "Network and Systems Administrator",
  "Network Engineer",
  "New Grad Software Engineer",
  "Nexus Engineer",
  "Nomad Engineer",
  "Notary Engineer",
  "Octopus Deploy Engineer",
  "OpenShift Engineer",
  "OpenStack Engineer",
  "Operations Engineer",
  "Oracle Developer",
  "Oracle SQL Developer",
  "Packer Engineer",
  "PHP Developer",
  "Powershell Engineer",
  "Principle Engineer in Artificial Intelligence",
  "Principle Engineer in Big Data",
  "Principle Engineer in Data Analysis",
  "Principle Engineer in Machine Learning",
  "Product Manager",
  "Production Support Engineer",
  "Programmer",
  "Prometheus Engineer",
  "Puppet Operations Engineer",
  "PyTest Engineer",
  "Python Developer",
  "Quality Assurance Specialist",
  "QA Engineer",
  "React Developer",
  "Robotics Engineer",
  "Ruby on rails Developer",
  "Salesforce Developer",
  "Search Engine Optimization",
  "Security Specialist",
  "Selenium Engineer",
  "Senior Ansible Development Engineer",
  "Senior Build and Release Engineer",
  "Senior Build Engineer",
  "Senior Cloud Architect",
  "Senior DevOps Architect",
  "Senior DevOps Engineer",
  "Senior DevSecOps Architect",
  "Senior DevSecOps Engineer",
  "Senior Site reliability Engineer",
  "Sharepoint Developer",
  "Site Reliability Engineer (Kubernetes – Docker)",
  "Software Engineer",
  "SonarQube Engineer",
  "Splunk Engineer",
  "Splunk Enterprise Security Engineer",
  "SQL Developer",
  "SRE Architect",
  "SRE Engineer",
  "Systems Administrator",
  "Tech Sales Engineer",
  "Technical Account Manager",
  "Technical Lead",
  "Terraform Engineer",
  "TFS Engineer",
  "Twistkock Engineer",
  "UDeploy Engineer",
  "UI DESIGNER",
  "UI Developer",
  "Unity Developer",
  "UX DESIGNER",
  "Vault Engineer",
  "Web Designer (UI/UX Designer)",
  "Web Developer",
  "WordPress Developer",
  "XL Deploy Engineer",
  "Zabbix Engineer",
];
let selectedSkills = [];

// Show suggestions based on input
skillsInput.addEventListener("input", () => {
  const inputValue = skillsInput.value.toLowerCase().trim();
  if (inputValue === "") {
    suggestionsList.style.display = "none";
    return;
  }

  const filteredSkills = availableSkills.filter(
    (skill) =>
      skill.toLowerCase().includes(inputValue) &&
      !selectedSkills.includes(skill)
  );

  if (filteredSkills.length > 0) {
    suggestionsList.innerHTML = filteredSkills
      .map((skill) => `<li class="suggestion-item">${skill}</li>`)
      .join("");
    suggestionsList.style.display = "block";
  } else {
    suggestionsList.style.display = "none";
  }
});

// Add a skill when a suggestion is clicked
suggestionsList.addEventListener("click", (e) => {
  if (e.target.classList.contains("suggestion-item")) {
    const skill = e.target.textContent.trim();
    addSkill(skill);
    skillsInput.value = ""; // Clear input after selection
    suggestionsList.style.display = "none"; // Hide suggestions
  }
});

// Add skill when Enter is pressed
skillsInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && skillsInput.value.trim()) {
    e.preventDefault();
    const skill = skillsInput.value.trim();
    addSkill(skill);
    skillsInput.value = ""; // Clear input after pressing Enter
  }
});

// Add skill function
function addSkill(skill) {
  if (!selectedSkills.includes(skill)) {
    selectedSkills.push(skill);

    const skillTag = document.createElement("div");
    skillTag.className = "skill-tag";
    skillTag.innerHTML = `${skill}<span class="remove-skill" onclick="removeSkill('${skill}')">&times;</span>`;

    selectedSkillsContainer.appendChild(skillTag);
    hiddenSkillsInput.value = selectedSkills.join(",");
  }
  toggleRequiredStyle();
}

function toggleRequiredStyle() {
  if (selectedSkills.length === 0) {
    skillsInput.classList.add("border-red-500", "focus:ring-red-500");
    skillsInput.setAttribute("required", "required");
  } else {
    skillsInput.classList.remove("border-red-500", "focus:ring-red-500");
    skillsInput.removeAttribute("required");
  }
}

// Remove skill function
function removeSkill(skill) {
  // Remove from selectedSkills array
  selectedSkills = selectedSkills.filter((s) => s !== skill);

  hiddenSkillsInput.value = selectedSkills.join(",");

  // Add the skill back to suggestions list
  if (!availableSkills.includes(skill)) {
    availableSkills.push(skill);
  }

  // Update the suggestions list with the newly available skill
  skillsInput.dispatchEvent(new Event("input"));

  // Remove the skill tag from the selected skills container
  const skillTags = Array.from(
    selectedSkillsContainer.getElementsByClassName("skill-tag")
  );
  skillTags.forEach((tag) => {
    if (tag.textContent.includes(skill)) {
      tag.remove();
    }
  });
  toggleRequiredStyle();
}

// Show popup for skills
function showPopup() {
  const popup = document.getElementById("popup");
  popup.style.display = "block";
  document.body.style.overflow = "hidden"; // Disable scrolling when popup is open
}

// Close popup for skills
function closePopup() {
  const popup = document.getElementById("popup");
  popup.style.display = "none";
  document.body.style.overflow = "auto"; // Enable scrolling again
}

// Close Post a Job Form
function closeForm() {
  const formContainer = document.querySelector(".form-container");
  formContainer.style.display = "none"; // Hide the form when close is clicked
}

// Hide suggestions when clicking outside
document.addEventListener("click", (e) => {
  if (!document.getElementById("skills-container").contains(e.target)) {
    suggestionsList.style.display = "none";
  }
});

function submitJobPost() {
  const form = document.getElementById("job-form");
  const inputs = form.querySelectorAll("input, select, textarea");
  let valid = true;

  // Loop through all the inputs to check if they are required and empty
  inputs.forEach((input) => {
    if (input.required && !input.value.trim()) {
      valid = false;
      input.style.borderColor = "red"; // Highlight the missing field
    } else {
      input.style.borderColor = ""; // Reset border if the field is filled
    }
  });

  // If the form is valid, submit it; otherwise, show an alert
  if (valid) {
    // If validation passes, submit the form manually
    form.submit();
  } else {
    alert("Please fill all required fields.");
  }
}
// pop up of post a job modal
// Open the modal when Get Started button is clicked

// document.addEventListener("DOMContentLoaded", () => {
function openModal() {
  document.getElementById("exampleModal").classList.remove("hidden");
}

// Close the modal (for the close button inside modal)
function closeModal() {
  document.getElementById("exampleModal").classList.add("hidden");
}
