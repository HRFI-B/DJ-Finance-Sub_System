function dynamicOption(){
    var tingkat_siswa = document.getElementById("tingkat_siswa").value;
    var kelas_siswa = document.getElementById("kelas_siswa");

    console.log("dynamicOption");

    kelas_siswa.options.length = 0;
    if (tingkat_siswa == "TK") {
        kelas_siswa.disabled = false;
        kelas_siswa.options.add(new Option("Kelas A Dahlia", "A DAHLIA"));
        kelas_siswa.options.add(new Option("Kelas A Melati", "A MELATI"));
        kelas_siswa.options.add(new Option("Kelas B Lily", "B LILY"));
        kelas_siswa.options.add(new Option("Kelas B Matahari", "B MATAHARI"));
    }
    else if(tingkat_siswa == "SD"){
        kelas_siswa.disabled = false;
        kelas_siswa.options.add(new Option("Kelas 1D", "1D"));
        kelas_siswa.options.add(new Option("Kelas 1J", "1J"));
        kelas_siswa.options.add(new Option("Kelas 1I", "1I"));
        kelas_siswa.options.add(new Option("Kelas 1P", "1P"));
        kelas_siswa.options.add(new Option("Kelas 2D", "2D"));
        kelas_siswa.options.add(new Option("Kelas 2J", "2J"));
        kelas_siswa.options.add(new Option("Kelas 2I", "2I"));
        kelas_siswa.options.add(new Option("Kelas 2P", "2P"));
        kelas_siswa.options.add(new Option("Kelas 3D", "3D"));
        kelas_siswa.options.add(new Option("Kelas 3J", "3J"));
        kelas_siswa.options.add(new Option("Kelas 3I", "3I"));
        kelas_siswa.options.add(new Option("Kelas 3P", "3P"));
        kelas_siswa.options.add(new Option("Kelas 4D", "4D"));
        kelas_siswa.options.add(new Option("Kelas 4J", "4J"));
        kelas_siswa.options.add(new Option("Kelas 4I", "4I"));
        kelas_siswa.options.add(new Option("Kelas 4P", "4P"));
        kelas_siswa.options.add(new Option("Kelas 5D", "5D"));
        kelas_siswa.options.add(new Option("Kelas 5J", "5J"));
        kelas_siswa.options.add(new Option("Kelas 5I", "5I"));
        kelas_siswa.options.add(new Option("Kelas 5P", "5P"));
        kelas_siswa.options.add(new Option("Kelas 6D", "6D"));
        kelas_siswa.options.add(new Option("Kelas 6J", "6J"));
        kelas_siswa.options.add(new Option("Kelas 6I", "6I"));
        kelas_siswa.options.add(new Option("Kelas 6P", "6P"));
    }

    else if(tingkat_siswa == "SMP"){
        kelas_siswa.disabled = false;
        kelas_siswa.options.add(new Option("Kelas 7D", "7D"));
        kelas_siswa.options.add(new Option("Kelas 7J", "7J"));
        kelas_siswa.options.add(new Option("Kelas 7I", "7I"));
        kelas_siswa.options.add(new Option("Kelas 7P", "7P"));
        kelas_siswa.options.add(new Option("Kelas 8D", "8D"));
        kelas_siswa.options.add(new Option("Kelas 8J", "8J"));
        kelas_siswa.options.add(new Option("Kelas 8I", "8I"));
        kelas_siswa.options.add(new Option("Kelas 8P", "8P"));
        kelas_siswa.options.add(new Option("Kelas 9D", "9D"));
        kelas_siswa.options.add(new Option("Kelas 9J", "9J"));
        kelas_siswa.options.add(new Option("Kelas 9I", "9I"));
        kelas_siswa.options.add(new Option("Kelas 9P", "9P"));
    }
}

function dynamicOptionDataPegawai(){
    var otoritas = document.getElementById("otoritas").value;
    var username = document.getElementById("username");
    var password = document.getElementById("password");

    if (otoritas == "Admin" || otoritas == "Staff") {
        username.disabled = false;
        password.disabled = false;
    }
    else {
        username.disabled = true;
        password.disabled = true;

        document.getElementsByName("username")[0].placeholder = "Disabled";
        document.getElementsByName("password")[0].placeholder = "Disabled";
    }
    
}