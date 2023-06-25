import { environment } from 'src/assets/envDev'
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DbsService {

  constructor(private http: HttpClient) { }

  getRace(): Observable<any> {
    const url = environment.baseURL + 'test'

    return this.http.get(url);
  }
}
