import { ApiService } from './../../../900_serviceo/api.service';
import { Component, Input, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-doi-output',
  templateUrl: './doi-output.component.html',
  styleUrls: ['./doi-output.component.scss'],
})
export class DoiOutputComponent {
  @Input() public DOI:string = ''
  public data:Array<any>|any

  constructor(
    private apiService:ApiService
  ) {}

  ngOnInit(): void {
    console.log('INIT DOI SHOW');

  }
  ngOnChanges(changes: SimpleChanges): void {
    //Called before any other lifecycle hook. Use it to inject dependencies, but avoid any serious work here.
    //Add '${implements OnChanges}' to the class.
    console.log('CHANGED DOI SHOW');
    if (this.DOI != '') {
      let dt: Array<any> | any = { doi:this.DOI };
      console.log('Consulta API');
      this.apiService.api_post('doi/metadata',dt).subscribe((res) => {
        this.data = res;
        console.log(res);
      });
    }
  }
}
