window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("header").style.padding = "20px 10px";
  } else {
    document.getElementById("header").style.padding = "0";
  }
}

