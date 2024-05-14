import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-doi-input',
  templateUrl: './doi-input.component.html',
  styleUrls: ['./doi-input.component.scss'],
})
export class DoiInputComponent {
  @Output() DOI: EventEmitter<string> = new EventEmitter<string>();
  public doiForm: FormGroup | any; // Criação do FormGroup

  ngOnInit() {
    this.doiForm = new FormGroup({
      doiNumber: new FormControl('10.5281/zenodo.159501'), // Cria um FormControl para o número do DOI
    });
  }

  onSubmit() {
    console.log(this.doiForm.value); // Ação para submissão do formulário
    this.DOI.emit(this.doiForm.value.doiNumber);
  }
}
function output(): (target: DoiInputComponent, propertyKey: "DOI") => void {
  throw new Error('Function not implemented.');
}
