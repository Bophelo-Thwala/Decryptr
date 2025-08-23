<h1>Hello, World</h1><br>
<h1 style="font-bold">COUNT : {$count}</h1><br><br>
<button on:click={Increment} class="IncreaseButton">Increment</button>
<button on:click={Decrement}>Decrement</button>
<button on:click={Reset}>Reset</button>
<script>
    import { writable } from "svelte/store";
    import './home.css';

    const count = writable(0);

    $: $count; // ensure $count is reactive

    function Increment() {
        $count++
    }

    function Decrement() {
        $count <= 0 ? $count = 0 : $count--;
    }

    function Reset() {
        $count = 0;
    }
</script>
