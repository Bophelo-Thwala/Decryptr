<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/decryptr-logo.png';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Decryptr - Converter, Encryption, Decryption</title>
	<meta name="description" content="It is a website where you can decrypt, encrypt and convert files">
</svelte:head>

{@render children?.()}
