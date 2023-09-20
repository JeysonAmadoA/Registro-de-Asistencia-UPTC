import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ElectronicEngineerComponent } from './electronic-engineer.component';

describe('ElectronicEngineerComponent', () => {
  let component: ElectronicEngineerComponent;
  let fixture: ComponentFixture<ElectronicEngineerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ElectronicEngineerComponent]
    });
    fixture = TestBed.createComponent(ElectronicEngineerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
