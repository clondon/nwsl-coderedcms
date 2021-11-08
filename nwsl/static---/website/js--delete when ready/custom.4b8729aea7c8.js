const  HeaderSection = document.querySelector(".hero_header_section");
const options = {
  root: null,   // The entire screen is the viewport
  threshold: "0",  // 0 to 1 value
  rootMargin: "0"

}


const observer = new IntersectionObserver(function
  (entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        hero_header_section.classList.add("hero_header_large");
        console.log(entry.target);
      } 
      
      

      
    
  });
}, options);

observer.observe(HeaderSection);

/* 
const sectionOneOptions = {
  rootMargin: "-200px 0px 0px 0px"
};

const sectionOneObserver = new IntersectionObserver(function(
  entries,
  sectionOneObserver
) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      header.classList.add("nav-scrolled");
    } else {
      header.classList.remove("nav-scrolled");
    }
  });
},
sectionOneOptions);

sectionOneObserver.observe(sectionOneObserver); */