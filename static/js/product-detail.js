const bigImg = document.querySelector(".big-img");
const smallImgs = document.querySelectorAll(".small-img");

const bigImgSrc = bigImg.getAttribute("src").split("/").at(-1);

smallImgs.forEach((img) => {
  if (img.getAttribute("src").split("/").find(src => src === bigImgSrc)) {
    img.classList.add("img--mark");
  }

  img.addEventListener("click", () => {
    const srcData = img.getAttribute("src")
    document.querySelector(".img--mark").classList.remove("img--mark");
    bigImg.setAttribute("src", srcData);
    img.classList.add("img--mark");
  })
});


const tabItem = document.querySelectorAll(".tab__item");
const tabContent = document.querySelectorAll(".tab__content");

tabItem.forEach((item) => {
  item.addEventListener("click", (event) => {
    document.querySelector(".border--bottom").classList.remove("border--bottom");
    item.classList.add("border--bottom");

    const content = document.querySelector("#" + item.dataset.tab);
    
    tabContent.forEach((t) => {
      t.classList.add("tab--hidden");
    })

    content.classList.remove("tab--hidden");

  })
})