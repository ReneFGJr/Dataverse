import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  http: any;
  constructor(
    private HttpClient: HttpClient,
    private cookieService: CookieService
  ) {}

  //public url: string = 'https://cip.brapci.inf.br/api/';
  public url: string = 'http://brp/api/';

  public api_post(type: string, dt: Array<any> = []): Observable<Array<any>> {
    let url = `${this.url}` + type;
    console.log(`Buscador: ${url}`);
    var formData: any = new FormData();
    let apikey = this.cookieService.get('section');
    formData.append('user', apikey);

    for (const key in dt) {
      formData.append(key, dt[key]);
    }

    return this.HttpClient.post<Array<any>>(this.url, formData).pipe(
      (res) => res,
      (error) => error
    );
  }
}
