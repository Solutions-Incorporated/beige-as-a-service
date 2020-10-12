<script lang="ts">
	import FileUploader from "./components/FileUploader.svelte";
</script>

<main>
	<h1>Beige-as-a-service</h1>
	
	<FileUploader />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>