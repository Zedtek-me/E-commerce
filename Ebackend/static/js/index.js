// display quick links
var links= document.querySelector('.b-seller')
function displayLink(){
    links.classList.toggle('buyer-seller')
}



// how it works
var detail= document.querySelector('.detail')
var detailParent= document.querySelector('.how-it-works')
const howItWorks= ()=>{
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

