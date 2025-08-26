<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
<script>
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { PUBLIC_PORT } from "$env/static/public";

    const PORT = PUBLIC_PORT;

    console.log("\nRunning SvelteKit on port", PORT);

    onMount(() => {
        setTimeout(() => {
            console.log("Redirecting to home page...");
            goto('/home');
        }, 3000); // Redirect after 3 seconds
    });
</script>
