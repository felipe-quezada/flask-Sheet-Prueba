const currentData = () => {
	let areaSelect = document.querySelector('#table'),
		printer = '';

	fetch('/list', { method: 'GET' })
		.then((res) => res.json())
		.then((data) => {
			data.forEach(
				(el) =>
					(printer += `
      <tr>
			<th>${el.id}</th>
			<td>${el.nombre}</td>
			<td>${el.edad}</td>
			<td>${el.profesion}</td>
      </tr>`)
			);
			areaSelect.innerHTML = printer;
		})
		.catch((err) => {
			window.location.href = '/error_page';
		});
};

const reloadPage = () => {
	window.location.href = '/';
};
