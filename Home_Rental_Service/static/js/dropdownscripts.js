var AddressObject = {
    "Dhaka": [
      "Dhaka","Gazipur","Kishoreganj","Manikganj","Munshiganj","Narayanganj","Narshingdi","Tangail","Faridpur","Gopalganj","Rajbari"
    ],
    "Sylhet": [
        "Sylhet","Moulovibazar","Sunamganj","Habiganj"

    ],
      
    "Rajshahi": [
        "Rajshahi","Sirajganj","Pabna","Bogura","Chapainawabganj","Naogaon","Joypurhat","Natore"

    ],

    "Chittagong": [
          "Chittagong","Cox's Bazar","Rangamati","Bandarban","Khagrachhari","Feni","Laksmipur","Comilla","Noakhali","Brahmanbaria","Chandpur"

    ],
    "Barshal": [
        "Barishal","Barguna","Bhola","Jhalokati","Patuakhali","pirojpur"
    ],
    "Khulna": [
        "Khulna","Bagerhat","Chuadanga","Jashore","Jhenaidah","Khustia","Magura","Narail","Satkhira"
    ],
    "Mymensingh":[
        "Mymensingh","Sherpur","Netrokona","Jamalpur"

    ],
    "Rongpur":[
        "Dinajpur","Nilfamari","Lalmonirhat","kurigram"

    ],

  }
  window.onload = function() {
    var divisionSel = document.getElementById("division");
    var districtSel = document.getElementById("district");
    var upazilaSel = document.getElementById("upazila");
    for (var x in AddressObject) {
      divisionSel.options[divisionSel.options.length] = new Option(x, x);
    }
   divisionSel.onchange = function() {
      //empty Chapters- and Topics- dropdowns
      districtSel.length = 1;
      //display correct values
        var z = AddressObject[this.value];
        for(var i=0;i<z.length;i++)
        {
            districtSel.options[districtSel.options.length] = new Option(z[i]);
        }
      }
    districtSel.onchange = function(){
      upazilaSel.length =  1;
    }
    }
    
  