import { ApiService } from './../../../900_serviceo/api.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-repatriation',
  templateUrl: './repatriation.component.html',
  styleUrls: ['./repatriation.component.scss'],
})
export class RepatriationComponent {
  public DOI:string = '';

  constructor(
    private apiService:ApiService
  ) {}

  updateDOI(data: string) {
    console.log(data);
    this.DOI = data;
  }
}
