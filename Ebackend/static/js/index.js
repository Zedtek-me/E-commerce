// display quick links
var links= document.querySelector('.b-seller')
var arrowDown= document.querySelector('.fa-angle-down')
function displayLink(){
    links.classList.toggle('buyer-seller')
    arrowDown.classList.toggle('fa-angle-down')
    arrowDown.classList.toggle('fa-angle-up')
}



// how it works
var detail= document.querySelector('.detail')
var detailParent= document.querySelector('.how-it-works')
const howItWorks= ()=>{
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

