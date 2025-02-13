// Separate data for recruiters, active users, and banned users
const totalRecruiters = [
  {
    id: "REC-101",
    name: "Aarav Sharma",
    company: "Innovative Solutions",
    phone: "+91 98765 43210",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  // Add more total recruiters data
  {
    id: "REC-101",
    name: "Aarav Sharma",
    company: "Innovative Solutions",
    phone: "+91 98765 43210",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-102",
    name: "Diya Mehta",
    company: "Talent Search Inc",
    phone: "+91 87654 32109",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-103",
    name: "Rohan Patel",
    company: "Global Workforce",
    phone: "+91 76543 21098",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-104",
    name: "Ananya Iyer",
    company: "Prime Recruiters",
    phone: "+91 65432 10987",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-105",
    name: "Kabir Gupta",
    company: "Elite Staffing Agency",
    phone: "+91 54321 09876",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-106",
    name: "Ishita Roy",
    company: "Future Talent Group",
    phone: "+91 43210 98765",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-107",
    name: "Aditya Nair",
    company: "Peak HR Solutions",
    phone: "+91 32109 87654",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-108",
    name: "Meera Khanna",
    company: "Next Level Recruitment",
    phone: "+91 21098 76543",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-109",
    name: "Krishna Joshi",
    company: "Global Staffing Experts",
    phone: "+91 10987 65432",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-110",
    name: "Sara Deshmukh",
    company: "Stellar HR Partners",
    phone: "+91 99876 54321",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-111",
    name: "Arjun Reddy",
    company: "Innovate Recruitment",
    phone: "+91 88765 43210",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-112",
    name: "Priya Menon",
    company: "Prime HR Hub",
    phone: "+91 77654 32109",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-113",
    name: "Vivaan Kapoor",
    company: "NextGen Talent",
    phone: "+91 66543 21098",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-114",
    name: "Shruti Aggarwal",
    company: "HR Connect",
    phone: "+91 55432 10987",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-115",
    name: "Ritika Jain",
    company: "Peak Staffing Solutions",
    phone: "+91 44321 09876",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-116",
    name: "Akash Verma",
    company: "Talent Innovations",
    phone: "+91 33210 98765",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-117",
    name: "Sanya Singh",
    company: "Global HR Partners",
    phone: "+91 22109 87654",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-118",
    name: "Yash Malhotra",
    company: "Stellar Workforce",
    phone: "+91 11098 76543",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "REC-119",
    name: "Pooja Bansal",
    company: "Innovative Hiring",
    phone: "+91 99887 65432",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
];

const activeUsers = [
  {
    id: "ACT-101",
    name: "Tanya Kapoor",
    company: "Tech Innovators",
    phone: "+91 98876 54310",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-102",
    name: "Vishal Rathi",
    company: "Web Dynamics",
    phone: "+91 87765 43211",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-103",
    name: "Simran Kapoor",
    company: "NextGen Software",
    phone: "+91 76654 32123",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-104",
    name: "Gaurav Chawla",
    company: "Global Tech Solutions",
    phone: "+91 65543 21034",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-105",
    name: "Nikita Sharma",
    company: "Creative Minds",
    phone: "+91 54432 10945",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-106",
    name: "Karan Yadav",
    company: "Bright Ideas Group",
    phone: "+91 43321 98756",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-107",
    name: "Rupal Agarwal",
    company: "HR Consulting Ltd.",
    phone: "+91 32210 87676",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-108",
    name: "Ravi Mehta",
    company: "Innovative Strategies",
    phone: "+91 21109 76567",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-109",
    name: "Harleen Kaur",
    company: "Tech Solutions",
    phone: "+91 10098 65489",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-110",
    name: "Pranav Singh",
    company: "Solutions Inc.",
    phone: "+91 99876 54301",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-111",
    name: "Sanjay Sharma",
    company: "Techie Group",
    phone: "+91 88765 43212",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-112",
    name: "Ananya Patel",
    company: "Business Boosters",
    phone: "+91 77654 32124",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-113",
    name: "Harshit Agarwal",
    company: "StartUp Innovations",
    phone: "+91 66543 21012",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-114",
    name: "Ridhima Joshi",
    company: "Future Leaders",
    phone: "+91 55432 10910",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-115",
    name: "Rashmi Gupta",
    company: "Innovate Group",
    phone: "+91 44321 09854",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-116",
    name: "Ashok Reddy",
    company: "Intelligent Networks",
    phone: "+91 33210 98709",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-117",
    name: "Bhavika Mehra",
    company: "Elite Consulting",
    phone: "+91 22109 87609",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-118",
    name: "Ankur Bansal",
    company: "Business Horizons",
    phone: "+91 11098 76534",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-119",
    name: "Manish Desai",
    company: "Global Reach Ltd.",
    phone: "+91 99887 65429",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-120",
    name: "Rohit Sharma",
    company: "Tech Ventures",
    phone: "+91 88776 54325",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
];

const bannedUsers = [
  {
    id: "REC-301",
    name: "Raghav Choudhary",
    company: "Future Solutions HR",
    phone: "+91 88776 54321",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  // Add more banned users data
  {
    id: "ACT-121",
    name: "Aarav Patel",
    company: "Quantum Technologies",
    phone: "+91 99876 54322",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-122",
    name: "Ria Khurana",
    company: "Tech Vision",
    phone: "+91 88765 43210",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-123",
    name: "Varun Kapoor",
    company: "Global Innovations",
    phone: "+91 77654 32109",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-124",
    name: "Sneha Joshi",
    company: "Pinnacle Solutions",
    phone: "+91 66543 21090",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-125",
    name: "Rajesh Mehta",
    company: "NextTech Ventures",
    phone: "+91 55432 10987",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-126",
    name: "Geeta Reddy",
    company: "Creative Innovations",
    phone: "+91 44321 09823",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-127",
    name: "Sandeep Kumar",
    company: "StartUp Minds",
    phone: "+91 33210 98712",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-128",
    name: "Priya Mehta",
    company: "Tech Guru",
    phone: "+91 22109 87654",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-129",
    name: "Siddharth Sharma",
    company: "Business Edge",
    phone: "+91 11098 76523",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-130",
    name: "Simran Verma",
    company: "Elite HR Solutions",
    phone: "+91 99887 65412",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-131",
    name: "Ravi Bansal",
    company: "Tech Bridge",
    phone: "+91 88776 54309",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-132",
    name: "Nisha Gupta",
    company: "Innovative HR",
    phone: "+91 77654 32101",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-133",
    name: "Karan Sharma",
    company: "StartSmart Solutions",
    phone: "+91 66543 21089",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-134",
    name: "Anjali Mehta",
    company: "Global Enterprise",
    phone: "+91 55432 10976",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-135",
    name: "Sahil Gupta",
    company: "Business Connect",
    phone: "+91 44321 09832",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-136",
    name: "Aishwarya Rathi",
    company: "Visionary Solutions",
    phone: "+91 33210 98703",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-137",
    name: "Anshika Sharma",
    company: "Dynamic Innovations",
    phone: "+91 22109 87632",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-138",
    name: "Puneet Singh",
    company: "Tech Experts",
    phone: "+91 11098 76511",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  {
    id: "ACT-139",
    name: "Neha Reddy",
    company: "Global Workforce",
    phone: "+91 99887 65403",
    img: "https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg",
  },
  // { id: 'ACT-140', name: 'Rohit Kumar', company: 'Innovative Strategies', phone: '+91 88776 54306', img: 'https://cdn.yellowmessenger.com/Xmnn1dek6nzZ1735637434099.jpeg' }
];

let currentCategory = totalRecruiters; // Default to totalRecruiters
let currentPage = 1;
const itemsPerPage = 10;

function renderProfiles(page) {
  const start = (page - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  const profilesToShow = currentCategory.slice(start, end);

  const profilesGrid = document.getElementById("profilesGrid");
  profilesGrid.innerHTML = "";

  profilesToShow.forEach((recruiter) => {
    const profileCard = `
            <div class="profile-card">
                <button class="more-options">
                    <i class="fas fa-ellipsis-v"></i>
                </button>
                <img src="${recruiter.img}" alt="${recruiter.name}">
                <h3>${recruiter.name}</h3>
                <div class="id">ID: ${recruiter.id}</div>
                <div class="company">${recruiter.company}</div>
                <div class="phone">${recruiter.phone}</div>
                <button class="view-profile" onclick="window.location.href='../html/Design CR Admin Freelancer view.html'">View Profile</button>
            </div>
        `;
    profilesGrid.innerHTML += profileCard;
  });
}

function renderPagination() {
  const totalPages = Math.ceil(currentCategory.length / itemsPerPage);
  const pagination = document.getElementById("pagination");
  pagination.innerHTML = "";

  // Add prev arrow
  const prevArrow = document.createElement("button");
  prevArrow.innerHTML = '<i class="fas fa-chevron-left"></i>';
  prevArrow.disabled = currentPage === 1;
  prevArrow.addEventListener("click", () => {
    if (currentPage > 1) {
      currentPage--;
      renderProfiles(currentPage);
      renderPagination();
    }
  });
  pagination.appendChild(prevArrow);

  // Add page numbers
  for (let i = 1; i <= totalPages; i++) {
    const pageButton = document.createElement("button");
    pageButton.textContent = i;
    if (i === currentPage) {
      pageButton.classList.add("active");
    }
    pageButton.addEventListener("click", () => {
      currentPage = i;
      renderProfiles(currentPage);
      renderPagination();
    });
    pagination.appendChild(pageButton);
  }

  // Add next arrow
  const nextArrow = document.createElement("button");
  nextArrow.innerHTML = '<i class="fas fa-chevron-right"></i>';
  nextArrow.disabled = currentPage === totalPages;
  nextArrow.addEventListener("click", () => {
    if (currentPage < totalPages) {
      currentPage++;
      renderProfiles(currentPage);
      renderPagination();
    }
  });
  pagination.appendChild(nextArrow);
}

// Toggle between sections: Total Recruiters, Active Users, and Banned Users
function highlightSection(sectionId) {
  // Clear previous highlights
  document.querySelectorAll(".stat-card").forEach((card) => {
    card.classList.remove("highlighted-section");
  });

  document.body.classList.remove(
    "highlight-total",
    "highlight-active",
    "highlight-banned"
  );

  // Set the current category
  if (sectionId === "totalRecruiters") {
    currentCategory = totalRecruiters;
    document.body.classList.add("highlight-total");
  } else if (sectionId === "activeUsers") {
    currentCategory = activeUsers;
    document.body.classList.add("highlight-active");
  } else if (sectionId === "bannedUsers") {
    currentCategory = bannedUsers;
    document.body.classList.add("highlight-banned");
  }

  // Highlight the selected section
  const selectedSection = document.getElementById(sectionId);
  selectedSection.classList.add("highlighted-section");

  // Reset pagination and profiles
  currentPage = 1;
  renderProfiles(currentPage);
  renderPagination();
}

// Initial render
renderProfiles(currentPage);
renderPagination();
