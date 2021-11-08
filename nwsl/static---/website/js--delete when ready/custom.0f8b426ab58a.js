const SectionOne = document.querySelector(".block-hero");
const options = {
  root: null,   //IS the viewport
  threshold: 0,  // 0 to 1 value
  rootMargin: "-150px" 

};
const observer = new IntersectionObserver(function
  (entries, observer) {
    entries.forEach(entry => {
      console.log(entry);
      entry.target.classList.toggle("header_size_control")
  });
}, options);

observer.observe(SectionOne);

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