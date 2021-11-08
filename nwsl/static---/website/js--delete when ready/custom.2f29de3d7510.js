const sectionOne = document.querySelector('#hero_header_section');

options = {};
const observer = new IntersectionObserver(function(entries, observer) {
  entries.forEach(entry => {
    console.log(entry)
;  })
 },options);

const sectionOneOptions = {
  rootMargin: "-200px 0px 0px 0px"
};

observer.observe(sectionOne);