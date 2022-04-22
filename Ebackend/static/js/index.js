// display quick links
function displayLink(){
    let links= document.querySelector('.b-seller')
    let arrowDown= document.querySelector('.fa-angle-down')
    links.classList.toggle('buyer-seller')
    arrowDown.classList.toggle('fa-angle-down')
    arrowDown.classList.toggle('fa-angle-up')
}


// "how it works"--> a hover effect that displays how a product works
const howItWorks= ()=>{
    let detail= document.querySelector('.detail')
    let detailParent= document.querySelector('.how-it-works')
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

// details about the cart functionality
const cartDetail= ()=>{
    var addToCart= document.querySelectorAll('.add-to-cart')//the add to cart parent
    var cart_detail= document.querySelectorAll('.cart-detail')//the details when hover 
    for(let j= 0; j<addToCart.length; j++){
        addToCart[j].addEventListener('mouseover', (e)=>{
            cart_detail[j].style.display='flex';
            setTimeout(()=>{cart_detail[j].style.display='none'}, 5000)})
            };
}
cartDetail()

// remove cart item button at the index page
const removeCartItem= ()=>{
    let removeCart= document.querySelectorAll('.remove-cart')
    let cart_count= document.querySelector('.cart-count')
    let cartForm= document.querySelectorAll('.cart-form')
    for(let j= 0; j<removeCart.length; j++){
        removeCart[j].addEventListener('click',(e)=>{
            cart_count.textContent=Number(cart_count.textContent)-1;//first, deduct 1 from the cart count.
            if(cart_count.textContent == 0){//if the count is deducted down to Zero, assign an empty string instead of 0
                cart_count.textContent= ''
            }
            const formInfo= new FormData(cartForm[j])
            fetch('/remove_from_cart/', {
                method:'POST',
                body: formInfo
            })
            .then((response)=>{console.log(response)})
            removeCart[j].style.display='none'//remove the button
        })
        
    }
}
removeCartItem()

// add to cart implementation
const cartCount= ()=>{
    let addToCart= document.querySelectorAll('.add-to-cart')/*the add to cart parent */
    let cart_count= document.querySelector('.cart-count')/*the cart content container--> increases in number when an item is added to cart*/
    let removeCart= document.querySelectorAll('.remove-cart')/*remove item from cart button */
    let cartForm= document.querySelectorAll('.cart-form')
    for(let j= 0; j<addToCart.length; j++){
        addToCart[j].addEventListener('click', (e)=>{
            // get product data when cart button is clicked;
            formInfo= new FormData(cartForm[j])
            // send data to backend for storage, and display at checkout.
            fetch('/add_to_cart/', {
                method:'POST',
                body: formInfo
            })
            .then((response)=>{console.log(response)})

            cart_count.textContent=Number(cart_count.textContent)+1;
            removeCart[j].style.display='flex';
            })
        }
}
cartCount()

// the toggles for editing each product.
const toggleEdit= ()=>{
    let toggleArrows= document.querySelectorAll('.prod-tog')
    let editDivs= document.querySelectorAll('.edits')
    for(let count= 0; count < toggleArrows.length; count++){
        toggleArrows[count].addEventListener('click', (e)=>{
            editDivs[count].classList.toggle('edit-options');
            toggleArrows[count].classList.toggle('fa-angle-up')
            toggleArrows[count].classList.toggle('fa-angle-down')
        })
    }
}
toggleEdit()

// display a preview of product uploaded by a vendor
function preView(){
    let img_file= document.querySelector('#product_img')
    let product_img= document.querySelector('.product_img')/*image tag to hold the image for a quick display*/
    img_file.addEventListener('change', (e)=>{
        product_img.src= URL.createObjectURL(e.target.files[0])
        product_img.style.display= 'flex'
    })
}
preView()


// form submission event for product removal
function removeProd(){
    let removeBtns= document.querySelectorAll('.remove-prod')
    let formBtns= document.querySelectorAll('#removeProd')
    for(let i= 0; i < removeBtns.length; i++){
        removeBtns[i].addEventListener('click', (e)=>{formBtns[i].click()})
    }

}
removeProd()