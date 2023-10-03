import {Component, EventEmitter, Input, Output} from '@angular/core';

@Component({
  selector: 'app-subject-list',
  templateUrl: './subject-list.component.html',
  styleUrls: ['./subject-list.component.scss']
})
export class SubjectListComponent {

  @Input() subjects: string[] = [];
  @Output() subjectSelected: EventEmitter<string> = new EventEmitter<string>();

  onSubjectSelected(selectedSubject: string) {
    this.subjectSelected.emit(selectedSubject);
  }
}
