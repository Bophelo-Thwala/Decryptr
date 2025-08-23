<Navbar />

<div>
   <ul>
        <a href="/home"><li><p>Profile</p></li></a>
   </ul>
</div>

<img src={LogoPhoto} alt="Logo" class="LogoPhoto"/>

<p class="Title">Decryptr</p>

<section class="About">
    <p id="AboutTitle">What is Decryptr?</p>

    <p id="AboutText">Decryptr is a decrypt and encrypt application. You can Decrypt files, Encrypt files 
        as well as Convert different files</p>
</section>

<!--
    <h1>Hello, World</h1><br>
    <h1 style="font-bold">COUNT : {$count}</h1><br><br>
    <button on:click={Increment} class="IncreaseButton">Increment</button>
    <button on:click={Decrement}>Decrement</button>
    <button on:click={Reset}>Reset</button>
-->


<Footer />
<script lang="ts">
    import { writable } from "svelte/store";
    import './home.css';
    import Navbar from "$lib/components/navbar.svelte";
    import Footer from "$lib/components/footer.svelte";
    import LogoPhoto from "$lib/assets/decryptr-logo.png";

    //const count = writable(0);
    let width = window.innerWidth;
    let height = window.innerHeight;

    /*
    $: $count; // ensure $count is reactive

    function Increment() {
        $count++
    }

    function Decrement() {
        $count <= 0 ? $count = 0 : $count--;
    }

    function Reset() {
        $count = 0;
    }*/

    console.log("Width: " + width);
    console.log("Height: " + height);
    console.log("Git");
</script>
