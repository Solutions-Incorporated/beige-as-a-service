<script lang="ts">
  let submitted = false;
  let promise = Promise.resolve([]);
  let files: string[] | Blob[];

  async function handleSubmit() {
    promise = uploadFile();
  }

  async function uploadFile() {
    if (files.length > 0) {
      submitted = true;
      const formData = new FormData();
      formData.append("file", files[0]);

      const response = await fetch("http://0.0.0.0:8000/color/what", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const hexCode = await response.json();

        const { scheme } = await mapColorScheme(hexCode);

        const results = async () =>
          await Promise.all(
            scheme.map(async (colorName) => {
              const { color } = await findByName(colorName);

              return { name: colorName, hexCode: color };
            })
          );

        const returnValue = await results().then((data) => data);

        return returnValue;
      } else {
        throw new Error("An error has occurred");
      }
    }
  }

  async function mapColorScheme(request) {
    const response = await fetch("http://0.0.0.0:8000/color/scheme", {
      method: "POST",
      body: JSON.stringify(request),
    });

    if (response.ok) {
      return await response.json();
    } else {
      throw new Error("An error has occurred");
    }
  }

  async function findByName(colorName) {
    const payload = JSON.stringify({ name: colorName });
    const response = await fetch("http://0.0.0.0:8000/color/name", {
      method: "POST",
      body: payload,
    });

    if (response.ok) {
      return await response.json();
    } else {
      throw new Error("An error has occurred");
    }
  }
</script>

<style>
  .box {
    width: 100px;
    height: 100px;
    border: 1px solid #000;
    margin: 0 auto;
  }

  .color-name {
    padding: 20px;
  }

  .wrapper {
    display: flex;
    flex-direction: column;
  }

  .color-container {
    display: inline-flex;
    width: 60%;
    justify-content: space-between;
    margin: 0 auto;
  }

  .container {
    display: flex;
    width: 60%;
    flex-direction: column;
    margin: 0 auto;
  }

  .preview {
    height: 80%;
    width: 80%;
    object-fit: contain;
    margin: 0 auto;
    padding-bottom: 20px; 
  }
</style>

<div class="container">
  {#if files}
    {#each files as file}
      <img src={URL.createObjectURL(file)} class="preview" />
    {/each}
  {/if}

  {#if submitted}
    {#await promise}
      <p>Calculating all of the colors for you...</p>
    {:then response}
      <div class="color-container">
        {#each response as color}
          <div class="wrapper">
            <div class="color-name">{color.name}</div>

            <div class="box" style="background-color:{color.hexCode}" />
          </div>
        {/each}
      </div>
    {:catch error}
      <p style="color: red">{error.message}</p>
    {/await}
  {/if}

  {#if !submitted}
    <form on:submit|preventDefault={handleSubmit}>
      <input required id="file" type="file" bind:files />
      <input type="submit" value="Upload file" />
    </form>
  {/if}
</div>
