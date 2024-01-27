$(function(){
    const radios = document.querySelectorAll(".topic");
    const n_month = document.querySelector("#n-month")

    $("#calculate").on("click",()=>{
        let c_count=0;
        let it = 0;
        for(let i=0; i < radios.length; i++){
                it = radios[i].checked?1:0;
                c_count += it;
        }
        var to_pay = c_count*(n_month.value)*(1000)
        console.log(c_count);
        if(n_month.value>9){
            to_pay = c_count*(10)*(1000)
        }
        $("#to-pay").text(to_pay)
        
    })
    
})