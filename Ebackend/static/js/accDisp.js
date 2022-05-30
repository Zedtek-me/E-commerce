// the diplay account number function-- useful at the payment page
const displayAcc= ()=>{
    let pointer= document.querySelector('#account-pointer')
    let accountNumber= document.querySelector('#acc-number')
    pointer.addEventListener('click', (e)=>{
        if (accountNumber.style.display == 'flex'){
            accountNumber.style.display= 'none'
        }
        else{
            accountNumber.style.display ='flex'
        }
    })
}

displayAcc()
