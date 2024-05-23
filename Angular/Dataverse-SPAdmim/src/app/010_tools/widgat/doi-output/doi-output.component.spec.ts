import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoiOutputComponent } from './doi-output.component';

describe('DoiOutputComponent', () => {
  let component: DoiOutputComponent;
  let fixture: ComponentFixture<DoiOutputComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DoiOutputComponent]
    });
    fixture = TestBed.createComponent(DoiOutputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
