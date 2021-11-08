const sectionOne = document.querySelector('#hero_header_section');

const options = {};


const observer = new IntersectionObserver(function(entries, observer) {
  entries.forEach(entry => {
    console.log(entry);
  })

}, options);

  

let callback = (entries, observer) => {
  entries.forEach(entry => {
    // Each entry describes an intersection change for one observed
    // target element:
    //   entry.boundingClientRect
    //   entry.intersectionRatio
    //   entry.intersectionRect
         if(entry.isIntersecting) {
           console.log("entry.isIntersecting");
         }

    //   entry.rootBounds
    //   entry.target
    //   entry.time
  });
};

 

let target = document.querySelector('#hero_header_section');
observer.observe(sectionOne);

