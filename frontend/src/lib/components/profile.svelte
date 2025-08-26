<script lang="ts">
    import './profile.css';
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

<img src="/default-avatar.jpg" alt="Profile" class="ProfilePhoto" on:click={ToggleDropDown} />

{#if isOpen}
    <div class="dropdown-menu" use:onClickOutside={CloseDropDown} transition:FadeAndSlide={{ y: -5, duration: 150}}>
        <ul>
            <a href="/home"><li><p>Profile</p></li></a>
            <a href="/home"><li><p>Dashboard</p></li></a>
        </ul>
    </div>
{/if}
