<script lang="ts">
  let disabled = false;
  let submitted = false;
	let promise = Promise.resolve([]);
  let files: string[] | Blob[];

  async function uploadFile() {
    if (files.length > 0) {
      submitted = true;
      const formData = new FormData();
      formData.append("file", files[0]);

      const response = await fetch("http://0.0.0.0:8000/color/what", {
        method: "POST",
        body: formData
      })
      
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("An error has occurred");
      }
    }
  }

  async function handleSubmit() {
    promise = uploadFile()
    disabled = true
  }
</script>

{#if files}
    {#each files as file}
        <img src="{URL.createObjectURL(file)}" class="preview" />
    {/each}
{/if}

{#if submitted}
  {#await promise}
    <p>Doing some quik mafs</p>
  {:then response}
    <div class="color-name">
      {response.color}
    </div>

    <div class="box" style="background-color:{response.color}"></div>
  {:catch error}
    <p style="color: red">{error.message}</p>
  {/await}
{/if}


{#if !submitted}
<form on:submit|preventDefault={handleSubmit} { disabled }>
  <input required id="file" type="file" bind:files />
  <input type="submit" value="Upload file" />
</form>
{/if}

<style>
    .box {
        width: 100px;
        height: 100px;
        border: 1px solid #000;
        margin: 0 auto;
    }

    .preview {
        max-height: 200px;
    }

    .color-name {
      padding: 20px;
    }
</style>

