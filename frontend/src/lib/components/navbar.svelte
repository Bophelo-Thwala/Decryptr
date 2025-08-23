<script lang="ts">
    import logo from '../assets/decryptr-logo.png';
    import Profile from './profile.svelte';
    import './navbar.css';

</script>

<header>
    <nav class="navigation">
       <a href="/home"><img src={logo} alt="Logo" class="Logo"/></a>

        <p>Convert</p>

        <p>Decrypt</p>

        <p>Encrypt</p>
        
        <p>API</p>

        <p>Pricing</p>

        <input placeholder="Search Here..." class="Search"/>

        <Profile />


    </nav>
</header>