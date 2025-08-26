<script lang="ts">
    import logo from '../assets/decryptr-logo.png';
    import Profile from './profile.svelte';
    import './navbar.css';
    import onClickOutside from '$lib/utils/onClickOutside';
	import { cubicOut } from 'svelte/easing';

    let isOpen = false;

    function FadeAndSlide(node: HTMLElement, { delay = 0, duration = 150, y = -5} = {}) {
        return {
            delay,
            duration,
            easing: cubicOut,
            css: (t: number) => `
                opacity: ${t};

                transform: translateY(${(1 - t) * y}px);
            `
           
        };
    }

    function ToggleDropDown() {
        isOpen = true;
    }

    function CloseDropDown() {
        isOpen = false;
    }

</script>

<header>
    <nav class="navigation">
       <a href="/home"><img src={logo} alt="Logo" class="Logo"/></a>

        <a href="/convert"><p>Convert</p></a>

        <a href="/decrypt"><p>Decrypt</p></a>

        <a href="/encrypt"><p>Encrypt</p></a>
        
        <a href="/api"><p>API</p></a>

        <a href="/pricing"><p>Pricing</p></a>

        <input placeholder="Search Here..." class="Search"/>

        <Profile />

    </nav>
</header>