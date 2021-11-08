const headerSection = document.getElementById('hero_header_section');
// headerSection.classList.add('.hero_header_large');

optionsHead = {
  root: null, //  The view point
  threshold: 1,
  rootMargin: "10px"
};
// console.log(options );
const headershrink = new IntersectionObserver(function(entries, headershrink)
{
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      headerSection.classList.remove('hero_header_small');
      headerSection.classList.add('hero_header_large');
    } else {
      headerSection.classList.remove('hero_header_large');
      headerSection.classList.add('hero_header_small');
    }
    
  });
}, optionsHead)

headershrink.observe(headerSection);

// Slide in phone number using animate.css library    animate__backInLeft

optionsContactItems = {
  root: null, //  The view point
  threshold: 1,
  rootMargin: "10px"
};

const ContactItemsDance = new IntersectionObserver(function(entries, contactDetailsDance)
{
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      headerSection.classList.remove('hero_header_small');
      headerSection.classList.add('hero_header_large');
    } else {
      headerSection.classList.remove('hero_header_large');
      headerSection.classList.add('hero_header_small');
    }
    
  });
}, optionsHead)

const contactDetailsDance = document.querySelectorAll("classPhoneAnimation");

// contactDetailsDanceObserver = new IntersectionObserverRatio((contactItems));


/* 
Const Options = {};


Const Observer = New Intersectionobserver(function(entries, Observer) {
  Entries.Foreach(entry => {
    Console.Log(entry);
  })

}, Options);

  

Let Callback = (Entries, Observer) => {
  Entries.Foreach(entry => {
    // Each Entry Describes an Intersection Change for One Observed
    // Target Element:
    //   Entry.Boundingclientrect
    //   Entry.Intersectionratio
    //   Entry.Intersectionrect
         If(entry.Isintersecting) {
           Console.Log("entry.Isintersecting");
         }

    //   Entry.Rootbounds
    //   Entry.Target
    //   Entry.Time
  });
};

 

Let Target = Document.Queryselector('#hero_header_section');
Observer.Observe(sectionone);

 */