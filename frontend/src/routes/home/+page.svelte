<Navbar />


<img src={LogoPhoto} alt="Logo" class="LogoPhoto"/>

<p class="Title">Decryptr</p>

<section class="About">
    <p id="AboutTitle">What is Decryptr?</p>

    <p id="AboutText">Decryptr is a decrypt and encrypt application. You can Decrypt files, Encrypt files 
        as well as Convert different files</p>
</section>


<Footer />
<script lang="ts">
    import { writable } from "svelte/store";
    import './home.css';
    import Navbar from "$lib/components/navbar.svelte";
    import Footer from "$lib/components/footer.svelte";
    import LogoPhoto from "$lib/assets/decryptr-logo.png";
	import { onMount } from "svelte";
    
    
    let width = writable(0);
    let height = writable(0);


    onMount(() => {
        width.set(window.innerWidth);
        height.set(window.innerHeight);
        console.log("Width: " + $width + "px");
        console.log("Height: " + $height + "px");      
    });

</script>
