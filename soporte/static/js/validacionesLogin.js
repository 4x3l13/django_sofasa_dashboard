const $frmLogin = document.getElementById('frmEncuestaIndex');
const $period = document.getElementById('period');
const $chart = document.getElementsByName('chart');


(function () {
    
    $frmLogin.addEventListener('submit',function(e){
        console.log($frmLogin)
        e.preventDefault();
        if ((String($period.value).trim()) == 0){
            alert("Hola");
            
        }else{

        }
    });
})();