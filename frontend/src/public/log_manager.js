const table=document.querySelector('tbody');

document.addEventListener("DOMContentLoaded",(event) => {
    console.log("script started");
    
    function add_log( log ){
        console.log("appending the following log")
        console.log(log);
        console.log("\n\n");
        row=`<tr>
        <td>${log.pitch}</td>
        <td>${log.roll}</td>
        <td>${log.yaw}</td>
        <td>${log.vgx}</td>
        <td>${log.vgy}</td>
        <td>${log.vgz}</td>
        <td>${log.templ}</td>
        <td>${log.temph}</td>
        <td>${log.tof}</td>
        <td>${log.h}</td>
        <td>${log.bat}</td>
        <td>${log.baro}</td>
        <td>${log.time}</td>
        <td>${log.agx}</td>
        <td>${log.agy}</td>
        <td>${log.agz}</td>
        </tr>`;
        table.insertAdjacentHTML('beforeend', row);
    }
    setInterval(function(){
        fetch('/fake_data').then(response => response.json()).then(add_log);
    },5000);
});