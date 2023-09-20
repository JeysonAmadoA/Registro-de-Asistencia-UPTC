import { Component } from '@angular/core';
const ELEMENT_DATA = [
  {
    'Nombre': 'Julio Malavida',
    'Correo': 'julio.malavida@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'María Perez',
    'Correo': 'maria.perez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': false,
  },
  {
    'Nombre': 'Carlos Rodríguez',
    'Correo': 'carlos.rodriguez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Ana López',
    'Correo': 'ana.lopez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Luisa Fernández',
    'Correo': 'luisa.fernandez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Pedro González',
    'Correo': 'pedro.gonzalez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': false,
  },
  {
    'Nombre': 'Sofía Torres',
    'Correo': 'sofia.torres@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Miguel Ramírez',
    'Correo': 'miguel.ramirez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Laura Herrera',
    'Correo': 'laura.herrera@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': false,
  },
  {
    'Nombre': 'Javier Rios',
    'Correo': 'javier.rios@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': false,
  },
  {
    'Nombre': 'Isabel Mendoza',
    'Correo': 'isabel.mendoza@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Ricardo Castro',
    'Correo': 'ricardo.castro@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Carmen Ortega',
    'Correo': 'carmen.ortega@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Antonio Silva',
    'Correo': 'antonio.silva@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Elena Navarro',
    'Correo': 'elena.navarro@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Mario Guzmán',
    'Correo': 'mario.guzman@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Natalia Vargas',
    'Correo': 'natalia.vargas@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre': 'Gabriel Castro',
    'Correo': 'gabriel.castro@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': false,
  },
  {
    'Nombre': 'Sara Jiménez',
    'Correo': 'sara.jimenez@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
  {
    'Nombre' : 'Daniel Ortega',
    'Correo': 'daniel.ortega@uptc.edu.co',
    'Programa': 'Ingeniería de Sistemas',
    '06/09/23': true,
  },
];
@Component({
  selector: 'app-teachers',
  templateUrl: './teachers.component.html',
  styleUrls: ['./teachers.component.scss']
})
export class TeachersComponent {
  columns: string[] = [
    'Nombre', 'Correo', 'Programa', '06/09/23'
  ];

  dataSource = ELEMENT_DATA;

  subjects: string[] = [
    'Materia 1',
    'Materia 2',
    'Materia 3'
  ]
}
